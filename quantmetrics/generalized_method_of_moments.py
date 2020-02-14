import numpy as np
import pandas as pd
import statsmodels.sandbox.regression.gmm as gmm


class gmm(gmm.GMM):
    def __init__(self, data_frame, y, x, z):
        self.data_frame = data_frame
        self.y = y
        self.x = x
        self.z = z

    def set_mcond(self, y, x, instrument):
        pass

    def fit_qm(self, start_param=None):
        '''
        set start parameter for gmm.fit method
        '''
        x_len = len(self.x)
        z_len = len(self.z)
        rhs_len = x_len + z_len

        if start_param is None:
            self.start_param = np.random.randn(rhs_len)
        else:
            self.start_param = start_param

        res = self.fit(start_params=self.start_param)

        return res

    def fit_gmm(self, y, x, instruments, dummy_vars=None, cross_terms=None):
        all_variables_list = [y] + x + instruments
        all_data = self.data_frame.get(all_variables_list)

        # for x: endogenous left hand side variables
        if cross_terms is not None:
            for ct in cross_terms:
                all_data[ct[0]+'#'+ct[1]] = all_data[ct[0]]*x[ct[1]]

        if dummy_vars is not None:
            for dv in dummy_vars:
                target = dv[0]
                dummy_component = dv[1]

                dummy_frame = pd.get_dummies(self.data_frame[target])
                dummy_frame = dummy_frame.get(dummy_component)
                all_data.join(dummy_frame)

        y = all_data.get([y])
        z = all_data.get(instruments)
        x = all_data.drop(y, axis=1).drop(instruments, axis=1)

        self.gmm_mod = self.gmm.GMM(endog=y, exog=x, instrument=z)
        self.res = self.gmm_mod.fit()

        return self.res
