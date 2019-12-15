import numpy
import pandas as pd
import os

from quantmetrics.core.frame import DataFrame
from quantmetrics.dataset import download_file 


def webuse(filename, return_data=True, stata_version=16):
    stata_url = 'http://www.stata-press.com/data/r%d/'%stata_version
    path_file = download_file(stata_url+filename+'.dta', filename)

    if return_data is True:
        return DataFrame(pd.read_stata(path_file))
