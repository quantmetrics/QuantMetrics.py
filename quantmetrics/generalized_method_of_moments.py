import numpy as np
import pandas as pd
import functools
from scipy.optimize import fmin


class gmm():
    def __init__(self, data_frame, y, x, z):
        self.data_frame = data_frame
        self.y = y
        self.x = x
        self.z = z

    def set_mcond(self, mcond, param_num):
        '''
        setting moment conditions
        mcond must be a function whose inputs are y, x, instrument(str), param
        '''
        self.mcond = mcond
        self.param_num = param_num

    def obj(self, param, A):
        x = self.mcond(self.y, self.x, self.z, param)
        return np.dot(x.T, np.dot(A, x))

    def two_step_est(self):
        self.weight = np.eye(len(self.z))
        self.res_first = fmin(self.obj, self.start_param, (self.weight, ))
        self.mcond_hat = self.mcond(self.y, self.x, self.z, self.res_first)
        self.weight = np.linalg.pinv(np.dot(self.mcond_hat, self.mcond_hat.T))
        self.res = fmin(self.obj, self.start_param, args=(self.weight, ))
        return self.res

    def fit(self, start_param=None):
        '''
        set start parameter for gmm.fit method
        '''
        z_len = len(self.z)
        if z_len < self.param_num:
            raise ValueError('Num of instruments must be larger than mcond')

        if start_param is None:
            self.start_param = np.random.randn(self.param_num).reshape([self.param_num, 1])
        else:
            self.start_param = start_param

        # optimization process
        res = self.two_step_est()

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
