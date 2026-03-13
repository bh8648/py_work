# numpy_modul.py

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(arr.shape)
print(arr.dtype)

zeros = np.zeros((3,3))
print(zeros)

ones = np.ones((2,4))
print(ones)

full = np.full((2,4), 7)
print(full)

a = np.concat([ones, full])
print(a.shape)
print(a)

b = np.concat([ones, full], axis=1)
print(b.shape)
print(b)


random = np.random.rand(3,3)
print(random)

randint = np.random.randint(1, 10, (3,3))
print(randint)

arr = np.array([1,2,3,4,5])
print(arr)
arr = arr+3
print(arr)
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())


# 브로드캐스팅 : 자동으로 차원을 맞춰서 늘려줌
arr1 = np.array([1,2,3])
arr2 = np.array([[1],[2],[3]])
result = arr1+arr2
print(result)
print(result.shape)


matrix1 = np.array([[1,2], [3,4]])
print(matrix1)
matrix2 = np.array([[5,6], [7,8]])
print(matrix2)

result = np.dot(matrix1, matrix2)
print(result)
print(result[1][1])
print(result[1,1])
print(result[:,:])


filtered = arr[arr>3]
print(filtered)

import pandas as pd

arr = np.array([1,2,3,4,5])
df = pd.DataFrame(arr, columns=['Value'])

print(df)
