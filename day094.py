x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)

x.shape
#(4,)

y.shape
#(5,)

x + y
# <type 'exceptions.ValueError'>: shape mismatch: objects 
#cannot be broadcast to a single shape

xx.shape
#(4, 1)

y.shape
#(5,)

(xx + y).shape
# (4, 5)

xx + y
'''
array([[ 1.,  1.,  1.,  1.,  1.],
       [ 2.,  2.,  2.,  2.,  2.],
       [ 3.,  3.,  3.,  3.,  3.],
       [ 4.,  4.,  4.,  4.,  4.]])
'''