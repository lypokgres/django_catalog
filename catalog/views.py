from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Category, Good


def index(request):
    categories_list = Category.objects.all()
    goods_list = Good.objects.all()
    paginator = Paginator(goods_list, 12)
    page = request.GET.get('page')
    # current_slug = page.strip('/').split('/')[-1]
    # filtered_goods = Good.objects.get()
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        goods = paginator.page(1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)
    context = {
        'goods': goods,
        'categories_list': categories_list
    }
    return render(request, 'catalog/index.html', context)


def good_page(request, url):
    item = url.strip('/').split('/')[-1]
    good = Good.objects.get(id=item)
    categories_list = Category.objects.all()
    context = {
        'good': good,
        'categories_list': categories_list
    }
    return render(request, 'catalog/good_page.html', context)