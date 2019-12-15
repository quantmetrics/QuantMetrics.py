import os
import urllib.request


_dataset_root = os.environ.get(
    'QUANTMETRICS_DATASET_ROOT',
    os.path.join(os.path.expanduser('~'), '.quantmetrics', 'dataset'))

def make_folder(folder_name):
    if not exist_file(folder_name):
        os.mkdir(folder_name)

def exist_file(path_of_file):
    return os.path.exists(path_of_file)

def download_file(url, file_name, save_folder=None):
    if not save_folder:
        make_folder('data')
        path_file = 'data/'+file_name

        if not exist_file(path_file):
            urllib.request.urlretrieve(url, path_file)

    else:
        make_folder(save_folder)
        path_file = save_folder+'/'+file_name

        if not exist_file(path_file):
            urllib.request.urlretrieve(url, path_file)

    return path_file
