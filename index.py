import numpy as np

import copy

a = np.arange(60)

a = a.reshape(5 , 12)

a = a.reshape(3 , 4 , 5)

# print(a)

b = a[2 , 2 , 0 : 2]

# print(b)

a[2] = 0

# print(a)

# print(b)

c= copy.deepcopy(a)

# print(c)

# print(c[1])

a[1] = 0

# print(a)
#### shouldn't be reflected in c
# print(c)