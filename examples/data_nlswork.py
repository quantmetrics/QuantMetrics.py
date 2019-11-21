from quantmetrics.core.frame import *
import urllib.request
import os
import pandas as pd


def main():
    save_folder = 'datasets'
    url = '	http://www.stata-press.com/data/r9/nlswork.dta'
    save_name = '/nlswork.dta'

    path_file = save_folder + save_name

    if not os.path.isdir(save_folder):
        os.mkdir(save_folder)

    if not os.path.isdir(save_folder+save_name):
        urllib.request.urlretrieve(url, save_folder+save_name)


    dataset = pd.read_stata(path_file)



if __name__ == '__main__':
    main()