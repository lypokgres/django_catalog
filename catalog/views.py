from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Category, Good


def index(request):
    categories_list = Category.objects.all()
    goods_list = Good.objects.all()
    paginator = Paginator(goods_list, 12)
    page = request.GET.get('page')
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        goods = paginator.page(1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)
    return render(request, 'catalog/index.html', {'categories_list': categories_list,
                                                  'goods': goods})


def good_page(request, url):
    item = url.strip('/').split('/')[-1]
    good = Good.objects.get(id=item)
    return render(request, 'catalog/good_page.html', {'good': good})
