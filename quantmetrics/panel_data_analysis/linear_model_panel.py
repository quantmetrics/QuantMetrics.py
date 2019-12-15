import statsmodels.api
import pandas as pd


class xtreg(statsmodels.api.OLS):
    def __init__(self, data_frame, reg_type='fe'):
        self.data_frame = data_frame

        if reg_type == 'fe':
            self.method = self.treg_fe
        elif reg_type == 're':
            self.method = self.treg_re
        

    def fit(self, y_name, x_list, dummy_variables=None, cross_terms=None, id=None, time=None):
        if id is None:
            pass
        else:
            self.id = id
        
        if time is None:
            pass
        else:
            self.time = time

        if self.time is not None:
            all_variables_list = x_list + y_name + self.id
        else:
            all_variables_list = x_list + y_name + self.id + self.time
            
        all_data = self.data_frame.get(all_variables_list)

        if cross_terms is not None:
            for ct in cross_terms:
                all_data[ct[0]+'#'+ct[1]] = all_data[ct[0]]*x[ct[1]]

        if dummy_variables is not None:
            for dv in dummy_variables:
                target = dv[0]
                dummy_component = dv[1]

                dummy_frame = pd.get_dummies(self.data_frame[target])
                dummy_frame = dummy_frame.get(dummy_component)
                all_data.join(dummy_frame)

        all_data_mean = all_data.groupby(self.id).mean()

        id_array = all_data[self.id].values
        all_data = all_data.drop(self.id)

        for id_idx in range(id_array):
            all_data.loc[id_idx] -= all_data_mean.loc[id_array[id_idx]]

        y = all_data.get([y_name])
        x = all_data.drop(y_name)

        OLS(y, x)



        






    def xtreg_fe(self):
        pass


    def xtreg_re(self):
        pass
