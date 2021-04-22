import numpy as np
from math import *
#zad.1
# a = np.arange(3, 9, 2)
# print(a)
# b = np.array([4, 6, 7])
# print(b)
# print(a * b)

# zad.3
# a = np.arange(3, 9, 2)
# print(a)
# b = np.array([4, 6, 7])
# print(b)
# print(a.dot(b))

# zad.4
# a = np.array([4, 6, 7])
# b = np.array([1, 9, 8])
# print(a * b)

# zad.5
# aa = []
# n = np.arange(6).reshape(2, 3)
# print(n)
# for x in n:
#     for y in x:
#         aa.append(sin(y))
# a = np.array([aa])
# print(a)
#
# # zad.6
# bb = []
# m = np.array([[4, 6, 7], [1, 4, 7]])
# print(m)
# for x in m:
#     for y in x:
#         bb.append(cos(y))
# b = np.array([bb])
# print(b)

# zad.8
# b = np.arange(9).reshape(3, 3)
# for x in b:
#     print(x)

# zad.9
b = np.arange(9).reshape(3, 3)
for x in b.flat:
    print(x)
    print("")

