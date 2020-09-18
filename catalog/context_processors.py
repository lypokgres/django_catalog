from catalog.models import Category


def not_nesting_categories(request):
    return {'categories_list': Category.objects.filter(parent=None)}
