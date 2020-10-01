from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def not_nesting_categories(categories):
    """Нахожу категории верхнего уровня у которых нет родителей"""
    return [category for category in categories if not category.parent_id]


def get_tree(categories, cat_list, lvl=0):
    """Строю дерево с категориями верхнего уровня"""
    tree = []
    for category in categories:
        child = get_children(category, cat_list)
        tree.append({
            'obj': category,
            'id': category.id,
            'parent_id': category.parent_id,
            'name': category.name,
            'slug': category.slug,
            'url': get_url_category(category, cat_list),
            'lvl': lvl,
            'child': get_tree(child, cat_list, lvl + 1)
        })
    return tree


def get_children(category, cat_list):
    """Нахожу детей текущей категории"""
    all_child = []
    for cat in cat_list:
        if category.pk == cat.parent_id:
            all_child.append(cat)
    return all_child


def get_parent(category, cat_list):
    """Нахожу родителя текущей категории"""
    for cat in cat_list:
        if category.parent_id == cat.pk:
            return cat


def find_all_children(category, cat_list):
    """Нахожу всех потомков категории"""
    all_children = [category]
    for cat in cat_list:
        if category.pk == cat.parent_id:
            all_children.extend(find_all_children(cat, cat_list))
    return all_children


def get_url_category(category, cat_list):
    if not get_parent(category, cat_list):
        return '/{}/'.format(category.slug)
    return '{}{}/'.format(get_url_category(get_parent(category, cat_list), cat_list), category.slug)


def get_category_img(category, cat_list):
    if category.image:
        return category.image.url.split('/')[-1]
    if get_parent(category, cat_list).image:
        return get_parent(category, cat_list).image.url.split('/')[-1]
    return "net-foto.png"


def pagination(request, goods_list, count_goods):
    page = request.GET.get('page')
    paginator = Paginator(goods_list, count_goods)
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        goods = paginator.page(1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)
    return goods


def get_good_tree(good_list, cat_list):
    tree = []
    for good in good_list:
        tree_element = {
            'name': good.name,
            'url': get_url_good(good, cat_list),
            'image': get_good_img(good, get_good_category(good, cat_list), cat_list)
        }
        tree.append(tree_element)
    return tree


def get_good_category(good, cat_list):
    for cat in cat_list:
        if cat.pk == good.category_id:
            return cat


def get_url_good(good, cat_list):
    category_url = get_url_category(get_good_category(good, cat_list), cat_list)
    return '{}{}_{}/'.format(category_url, good.slug, good.id)


def get_good_img(good, category, cat_list):
    if good.image:
        return good.image.url.split('/')[-1]
    return get_category_img(category, cat_list)
