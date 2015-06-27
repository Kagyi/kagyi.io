
def get_items_from_python_file(module):
    items = [item for item in dir(module) if not item.startswith("__")]
    all_items = []
    for item in items:
        item_info = getattr(module, item)
        item_name = item.replace('_', '-')
        item_link = '/learn/' + item_name
        item_info['link'] = item_link
        item_info['name'] = item_name
        all_items.append (item_info)
    return all_items
