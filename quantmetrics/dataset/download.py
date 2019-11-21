import os
import urllib.request


_dataset_root = os.environ.get(
    'QUANTMETRICS_DATASET_ROOT',
    os.path.join(os.path.expanduser('~'), '.quantmetrics', 'dataset'))

def make_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def download_file(url, file_name, save_folder=None):
    if not save_folder:
        make_folder('data')
        urllib.request.urlretrieve(url, 'data/'+file_name)
    else:
        make_folder(save_folder)
        urllib.request.urlretrieve(url, save_folder+'/'+file_name)
