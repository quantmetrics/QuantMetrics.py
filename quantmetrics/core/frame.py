import pandas as pd


class DataFrame(pd.DataFrame):
    def __init__(self, data=None, index=None, columns=None, dtype=None, copy=False):
        super().__init__(data=data, index=index, columns=columns, dtype=dtype, copy=copy)
        pd.set_option('display.max_columns', 50)

    def xtset(self, id=None, time=None):
        self.id = id
        self.time = time
