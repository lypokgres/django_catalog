def find_child(category):
    if not category.child.all():
        return [category]
    all_child = []
    all_child.extend(category.child.all())
    for child in all_child:
        all_child.extend(child.child.all())
        find_child(child)
    return all_child
