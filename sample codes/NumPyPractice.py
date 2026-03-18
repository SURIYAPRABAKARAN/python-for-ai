import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(arr * 2)
print(arr.shape)
print(arr.size)
print(arr.dtype)

matrix = np.array([[1],[1],[1]])
print(matrix)
print(matrix * 2)
print(matrix.shape)
print(matrix.size)
print(matrix.dtype)

arr = np.array([10,20,30,40,50])

print(arr[2])
print(arr[1:4])
print(arr[0:5:5])

arr = np.array([5,10,15,20,25,30])
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[0:5:2])
print(arr.reshape(2,3))
print(arr.reshape(3,2))
print(arr.reshape(6,1))

arr = np.array([2,4,6,8])
arr1 = np.array([1,1,1,1])
print(arr + 10)
print(arr * 5)
print(arr + arr1)

num = np.random.rand()
print(num)

arr = np.random.rand(5)

print(arr)

arr = np.random.randint(1,10,5)

print(arr)

matrix = np.random.randint(1,101,(3,9))

print(matrix)

numbers = [1,2,2,3,3,3]

count = {}
for num in numbers:
    count[num] = count.get(num, 0) + 1

print(count)