import pandas as pd


class DataFrame(pd.DataFrame):
    def __init__(self):
        print(1)

    def tsset(self, x, y):
        return x, y