import os

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

def get_submissions_path(app_root):
    return os.getenv('OPENSHIFT_DATA_DIR',
                     os.path.join(app_root, 'submissions'))

def get_config_file(app_root):
    if os.getenv('OPENSHIFT_DATA_DIR'):
        return os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'config.py')
    return 'config.py'
