from django.shortcuts import render, get_object_or_404
from .models import Category, Good
from .utils import find_all_children, pagination, get_url_category, get_good_tree
from django.http import Http404


def index(request):
    cat_list = Category.objects.all()
    goods_list = get_good_tree(Good.objects.all(), cat_list)
    context = {'goods': pagination(request, goods_list, 12)}
    return render(request, 'catalog/index.html', context)


def categories(request, path=''):
    categories_list = Category.objects.all()
    slug_list = path.split('/')
    current_category = get_object_or_404(Category, slug=slug_list[-1])
    if path not in get_url_category(current_category, categories_list):
        raise Http404
    category_children = find_all_children(current_category, categories_list)
    goods_list = get_good_tree(Good.objects.filter(category__in=category_children + [current_category]), categories_list)
    breadcrumbs = reversed([category for category in current_category.find_parent()])
    context = {
        'goods': pagination(request, goods_list, 12),
        'current_category': current_category,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'catalog/index.html', context)


def good_page(request, pk):
    good = get_object_or_404(Good, id=pk.strip('/'))
    if request.path not in good.get_absolute_url():
        raise Http404
    breadcrumbs = reversed([category for category in good.find_parent()])
    context = {'good': good, 'breadcrumbs': breadcrumbs}
    return render(request, 'catalog/good_page.html', context)


def search(request):
    cat_list = Category.objects.all()
    goods_list = []
    search_text = ''
    if request.GET.get('search'):
        search_text = request.GET.get('search')
        goods_list = get_good_tree(Good.objects.filter(name__icontains=search_text), cat_list)

    context = {
        'goods_list': pagination(request, goods_list, 12),
        'search_text': search_text
    }
    return render(request, 'catalog/search.html', context)
