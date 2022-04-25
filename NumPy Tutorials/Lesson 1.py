>>> import numpy as np
>>> a = np.array([1, 2, 3, 4])
>>> a.dtype
# dtype('int32')
>>> a = np.array([1, 2, "3", True])
>>> a
# array(['1', '2', '3', 'True'], dtype='<U11')
>>> a[0]
# '1'
>>> a[1]
# '2'
>>> a[1] = '123'
>>> a
# array(['1', '123', '3', 'True'], dtype='<U11')
>>> a[1] = 234
>>> a
# array(['1', '234', '3', 'True'], dtype='<U11')
>>> a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a[2]
# 3
>>> a[ [1, 1, 1, 1, 1, 1, 1, 1, 1,] ]
# array([2, 2, 2, 2, 2, 2, 2, 2, 2])
>>> a [ [1, 1, 1, 1, 1,] ]
# array([2, 2, 2, 2, 2])
>>> a[[ True, True, False, False, False, False, True, True, True ]]
# array([1, 2, 7, 8, 9])
>>> b = a.reshape(3, 3)
>>> b
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
>>> b[1][2]
# 6
>>> b[1, 2]
# 6
