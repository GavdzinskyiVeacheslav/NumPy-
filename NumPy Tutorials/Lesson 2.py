>>> import numpy as np
>>> a = np.array([1, 2, 3, 4])
>>> a = np.array([1, 2, 3, 4], 'float64')
>>> a
# array([1., 2., 3., 4.])
>>> np.sctypeDict
#{'?': <class 'numpy.bool_'>, 0: <class 'numpy.bool_'>, 'byte': <class 'numpy.int8'>, 'b': <class 'numpy.int8'>, 1: <class 'numpy.int8'>, 'ubyte': <class 'numpy.uint8'>, 'B': <class 'numpy.uint8'>, 2: <class 'numpy.uint8'>, 'short': <class 'numpy.int16'>, 'h': <class 'numpy.int16'>, 3: <class 'numpy.int16'>, 'ushort': <class 'numpy.uint16'>, 'H': <class 'numpy.uint16'>, 4: <class 'numpy.uint16'>, 'i': <class 'numpy.intc'>, 5: <class 'numpy.intc'>, 'uint': <class 'numpy.uint32'>, 'I': <class 'numpy.uintc'>, 6: <class 'numpy.uintc'>, 'intp': <class 'numpy.int64'>, 'p': <class 'numpy.int64'>, 9: <class 'numpy.int64'>, 'uintp': <class 'numpy.uint64'>, 'P': <class 'numpy.uint64'>, 10: <class 'numpy.uint64'>, 'long': <class 'numpy.int32'>, 'l': <class 'numpy.int32'>, 7: <class 'numpy.int32'>, 'L': <class 'numpy.uint32'>, 8: <class 'numpy.uint32'>, 'longlong': <class 'numpy.int64'>, 'q': <class 'numpy.int64'>, 'ulonglong': <class 'numpy.uint64'>, 'Q': <class 'numpy.uint64'>, 'half': <class 'numpy.float16'>, 'e': <class 'numpy.float16'>, 23: <class 'numpy.float16'>, 'f': <class 'numpy.float32'>, 11: <class 'numpy.float32'>, 'double': <class 'numpy.float64'>, 'd': <class 'numpy.float64'>, 12: <class 'numpy.float64'>, 'longdouble': <class 'numpy.longdouble'>, 'g': <class 'numpy.longdouble'>, 13: <class 'numpy.longdouble'>, 'cfloat': <class 'numpy.complex128'>, 'F': <class 'numpy.complex64'>, 14: <class 'numpy.complex64'>, 'cdouble': <class 'numpy.complex128'>, 'D': <class 'numpy.complex128'>, 15: <class 'numpy.complex128'>, 'clongdouble': <class 'numpy.clongdouble'>, 'G': <class 'numpy.clongdouble'>, 16: <class 'numpy.clongdouble'>, 'O': <class 'numpy.object_'>, 17: <class 'numpy.object_'>, 'S': <class 'numpy.bytes_'>, 18: <class 'numpy.bytes_'>, 'unicode': <class 'numpy.str_'>, 'U': <class 'numpy.str_'>, 19: <class 'numpy.str_'>, 'void': <class 'numpy.void'>, 'V': <class 'numpy.void'>, 20: <class 'numpy.void'>, 'M': <class 'numpy.datetime64'>, 21: <class 'numpy.datetime64'>, 'm': <class 'numpy.timedelta64'>, 22: <class 'numpy.timedelta64'>, 'bool8': <class 'numpy.bool_'>, 'b1': <class 'numpy.bool_'>, 'int64': <class 'numpy.int64'>, 'i8': <class 'numpy.int64'>, 'uint64': <class 'numpy.uint64'>, 'u8': <class 'numpy.uint64'>, 'float16': <class 'numpy.float16'>, 'f2': <class 'numpy.float16'>, 'float32': <class 'numpy.float32'>, 'f4': <class 'numpy.float32'>, 'float64': <class 'numpy.float64'>, 'f8': <class 'numpy.float64'>, 'complex64': <class 'numpy.complex64'>, 'c8': <class 'numpy.complex64'>, 'complex128': <class 'numpy.complex128'>, 'c16': <class 'numpy.complex128'>, 'object0': <class 'numpy.object_'>, 'bytes0': <class 'numpy.bytes_'>, 'str0': <class 'numpy.str_'>, 'void0': <class 'numpy.void'>, 'datetime64': <class 'numpy.datetime64'>, 'M8': <class 'numpy.datetime64'>, 'timedelta64': <class 'numpy.timedelta64'>, 'm8': <class 'numpy.timedelta64'>, 'int32': <class 'numpy.int32'>, 'i4': <class 'numpy.int32'>, 'uint32': <class 'numpy.uint32'>, 'u4': <class 'numpy.uint32'>, 'int16': <class 'numpy.int16'>, 'i2': <class 'numpy.int16'>, 'uint16': <class 'numpy.uint16'>, 'u2': <class 'numpy.uint16'>, 'int8': <class 'numpy.int8'>, 'i1': <class 'numpy.int8'>, 'uint8': <class 'numpy.uint8'>, 'u1': <class 'numpy.uint8'>, 'complex_': <class 'numpy.complex128'>, 'int0': <class 'numpy.int64'>, 'uint0': <class 'numpy.uint64'>, 'single': <class 'numpy.float32'>, 'csingle': <class 'numpy.complex64'>, 'singlecomplex': <class 'numpy.complex64'>, 'float_': <class 'numpy.float64'>, 'intc': <class 'numpy.intc'>, 'uintc': <class 'numpy.uintc'>, 'int_': <class 'numpy.int32'>, 'longfloat': <class 'numpy.longdouble'>, 'clongfloat': <class 'numpy.clongdouble'>, 'longcomplex': <class 'numpy.clongdouble'>, 'bool_': <class 'numpy.bool_'>, 'bytes_': <class 'numpy.bytes_'>, 'string_': <class 'numpy.bytes_'>, 'str_': <class 'numpy.str_'>, 'unicode_': <class 'numpy.str_'>, 'object_': <class 'numpy.object_'>, 'int': <class 'numpy.int32'>, 'float': <class 'numpy.float64'>, 'complex': <class 'numpy.complex128'>, 'bool': <class 'numpy.bool_'>, 'object': <class 'numpy.object_'>, 'str': <class 'numpy.str_'>, 'bytes': <class 'numpy.bytes_'>, 'a': <class 'numpy.bytes_'>}
>>> a = np.array([1, 2, 3, 4], 'uintc')
>>> a
# array([1, 2, 3, 4], dtype=uint32)
>>> a = np.array([1, 2, 3, 4], 'str_')
>>> a
# array(['1', '2', '3', '4'], dtype='<U1')
>>> np.complex64(10)
# (10+0j)
>>> np.int16(10.5)
# 10
>>> a = np.array([1, 2, 5000, 1000], dtype='int8')
>>> a
# array([   1,    2, -120,  -24], dtype=int8)
>>> a = np.array([1, 2, 5000, 1000])
>>> a
# array([   1,    2, 5000, 1000])
>>> np.complex64(a)
# array([1.e+00+0.j, 2.e+00+0.j, 5.e+03+0.j, 1.e+03+0.j], dtype=complex64)
>>> a
# array([   1,    2, 5000, 1000])
>>> b = np.complex64(a)
>>> c = np.int32(b)
# <input>:1: ComplexWarning: Casting complex values to real discards the imaginary part
>>> c
# array([   1,    2, 5000, 1000])
>>> np.array("Hello")
# array('Hello', dtype='<U5')
>>> a = np.array([[1, 2], [3, 4], [5, 6]])
>>> a
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
>>> a = np.array([[1, 2], [3, 4], [5, 6, 7]])
# <input>:1: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
>>> b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
>>> b
# array([[[ 1,  2],
#         [ 3,  4]],
#        [[ 5,  6],
#         [ 7,  8]],
#        [[ 9, 10],
#         [11, 12]]])
>>> b[0]
# array([[1, 2],
#        [3, 4]])
>>> b[1]
# array([[5, 6],
#        [7, 8]])
>>> b[2]
# array([[ 9, 10],
#        [11, 12]])
>>> b[0, 0]
# array([1, 2])
>>> b[0, 0, 0]
# 1
























