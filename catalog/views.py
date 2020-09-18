from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Category, Good
from .utils import find_child
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse


def index(request, path=''):
    goods_list = Good.objects.all()
    page = request.GET.get('page')
    search = request.GET.get('search')
    current_category = '/'
    breadcrumbs = None

    if search:
        goods_list = goods_list.filter(name__icontains=search)

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
        'current_category': current_category,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'catalog/index.html', context)


def good_page(request, pk):
    good = Good.objects.get(id=pk.strip('/'))
    breadcrumbs = [category for category in good.find_parent()]
    breadcrumbs.reverse()
    search = request.GET.get('search')

    if search:
        return redirect(reverse('index'), kwargs={'search': search})

    context = {
        'good': good,
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'catalog/good_page.html', context)
