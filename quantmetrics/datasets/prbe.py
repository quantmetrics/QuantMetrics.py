import zipfile
import os
import zipfile

import progressbar
from six.moves.urllib import request


url = 'https://www.upjohn.org/sites/default/files/2019-02/PA_ReempBonus.zip'

def get_prbe(path='.'):
    request.urlretrieve(url, path+'prbe.zip')

    # Unzip the file
    zf = zipfile.ZipFile(path+'prbe.zip')
    for name in zf.namelist():
        dirname, filename = os.path.split(name)
        if not filename == '':
            zf.extract(name, './examples/datasets')
    os.remove(path+'prbe.zip')

    