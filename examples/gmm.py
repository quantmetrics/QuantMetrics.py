import quantmetrics.datasets
import quantmetrics.generalized_method_of_moments as gm

docvisits = quantmetrics.datasets.webuse('docvisits')
print(docvisits.head())

y = 'docvis'
x = ['private', 'chronic', 'female', 'income']
z = ['private', 'chronic', 'female', 'age', 'black', 'hispanic']

mod = gm.gmm(docvisits, y, x, z)
print(mod)
res = mod.fit_qm()
print(res)
'''
AttributeError: 'gmm' object has no attribute 'momcond'
statsmodels0.11.0ではmomentconditionが実装されておらず、GMMは実行できない
'''
# TODO:implement GMM by yourself.
