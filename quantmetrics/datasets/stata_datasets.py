import numpy

from quantmetrics.dataset import download_file 


def webuse(filename):
    stata_url = 'http://www.stata-press.com/data/r16/'
    download_file(stata_url+filename+'.dta', filename)
    return
