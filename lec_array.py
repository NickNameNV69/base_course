import numpy as np

a = [1, 2, 4]

b = np.array(a)

print(type(a))  #<class 'list'>
print(type(b))  #<class 'numpy.ndarray'>

print(b * b)    #[ 1  4 16]
print(b / b)    #[1. 1. 1.]
print(b - b)    #[0 0 0]

#print(a - a)   TypeError: unsupported operand type(s) for -: 'list' and 'list'

b = np.append(b, 'good')
print(b)    #['1' '2' '4' 'good']

b = np.append(b, 1)
print(b)    #['1' '2' '4' 'good' '1']