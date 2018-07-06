# Problem

```
The problem is also known as 'Maximum Sub Square Matrix' -
Given a matrix of 0s and 1s, find the biggest sub-square matrix entirely of 1s.
```

# Solution

![https://youtube.com/watch?v=FO7VXDfS8Gk](https://img.youtube.com/vi/FO7VXDfS8Gk/0.jpg "")

# Documentation

## Morpho Math

- http://scipy-lectures.org/advanced/image_processing/#mathematical-morphology
- https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.ndimage.morphology.generate_binary_structure.html
- https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.ndimage.morphology.binary_erosion.html#scipy.ndimage.morphology.binary_erosion
- https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.count_nonzero.html#numpy-count-nonzero
- https://programcreek.com/python/example/102210/numpy.count_nonzero

### Experimentations

```python
>>> import numpy as np
>>> a = 1 - np.zeros((5,4), dtype=np.int)
>>> a[2, 0] = a[4, 0] = a[0, 1] = a[4, 1] = a[4, 2] = a[0,3] = 0

>>> struct = ndimage.generate_binary_structure(2, 1)
>>> struct[0, :] = False
>>> struct[:, 0] = False
>>> struct[2, 2] = True
In [34]: struct
Out[34]:
array([[False, False, False],
       [False,  True,  True],
       [False,  True,  True]])

In [66]: ndimage.binary_erosion(a, structure=struct).astype(a.dtype)
Out[66]:
array([[0, 0, 0, 0],
       [0, 1, 1, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]])

In [69]: ndimage.binary_erosion(a, structure=struct, iterations=2).astype(a.dtype)
Out[69]:
array([[0, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]])

In [72]: np.count_nonzero(ndimage.binary_erosion(a, structure=struct, iterations=2).astype(a.dtype))
Out[72]: 1
```