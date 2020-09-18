from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Category, Good
from .utils import find_child
from django.http import Http404


def index(request, path=''):
    categories_list = Category.objects.filter(parent=None)
    goods_list = Good.objects.all()
    page = request.GET.get('page')
    current_category = '/'
    breadcrumbs = None

    if path:
        path = path.split('/')
        current_category = Category.objects.get(slug=path[-1])
        category_child = find_child(current_category)
        goods_list = goods_list.filter(category=current_category) | goods_list.filter(category__in=category_child)
        breadcrumbs = [category for category in current_category.find_parent()]
        breadcrumbs.reverse()
        for category in current_category.find_parent():
            if category.slug not in path:
                raise Http404

    paginator = Paginator(goods_list, 12)
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        goods = paginator.page(1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)
    context = {
        'goods': goods,
        'categories_list': categories_list,
        'current_category': current_category,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'catalog/index.html', context)


def good_page(request, pk):
    path = request.path.strip('/').split('/')[:-1]
    good = Good.objects.get(id=pk.strip('/'))
    categories_list = Category.objects.filter(parent=None)
    breadcrumbs = [category for category in good.find_parent()]
    breadcrumbs.reverse()
    context = {
        'good': good,
        'categories_list': categories_list,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'catalog/good_page.html', context)
