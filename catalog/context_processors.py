from catalog.models import Category
from catalog.utils import get_tree, get_flat_tree, not_nesting_categories


def categories(request):
    cat_list = Category.objects.all()
    return {'categories_list': get_tree(not_nesting_categories(cat_list), cat_list)}
