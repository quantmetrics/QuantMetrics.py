import numpy as np
import pandas as pd
import quantmetrics.datasets
import quantmetrics.generalized_method_of_moments as gmm

docvisits = quantmetrics.datasets.webuse('docvisits')

y = ['docvis']
x = ['private', 'chronic', 'female', 'income']
z = ['private', 'chronic', 'female', 'age', 'black', 'hispanic']

'''
AttributeError: 'gmm' object has no attribute 'momcond'
statsmodels0.11.0ではmomentconditionが実装されておらず、GMMは実行できない
'''

mod = gmm.gmm(docvisits, y, x, z)

def mcond(y, x, z, param):
    Y = docvisits[y].values
    X = np.insert(docvisits[x].values, 0, 1, axis=1)
    param = param.reshape([X.shape[1], 1])
    resid = Y - np.exp(np.dot(X, param))
    Z = docvisits[z].values
    return np.dot(Z.T, resid)



mod.set_mcond(mcond, len(x)+1)
init = np.array([-0.5, 0.53, 1.1, .66, .013]).reshape([5,1])
res = mod.fit(init)
print(res)
# const private chronic female income
# 0.57 2.3 3.5 -0.81 0.004
# stataの結果と異なる→初期値の依存性？
# 最適化関数の違い？
