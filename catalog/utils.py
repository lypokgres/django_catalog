def find_child(category):
    if not category.child.all():
        return [category]
    all_child = []
    all_child.extend(category.child.all())
    for child in all_child:
        all_child.extend(child.child.all())
        find_child(child)
    return all_child


def find_parent(item):
    parents = [item]
    if item.parent:
        parent = item.parent
        parents.extend(find_parent(parent))
    return parents
