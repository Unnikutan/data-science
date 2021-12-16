#dot product


import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
value = list(map(int, input().split()))
value1=list(map(int, input().split()))

matrix = np.array(value).reshape(a,b)
matrix1 = np.array(value1).reshape(a,b)
print("first matrix :" ,matrix)
print("second matrix :",matrix1)
z=np.dot(matrix,matrix1)
print("dot product : ",z)


# transpose


import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
value = list(map(int, input().split()))

matrix = np.array(value).reshape(a,b)

print("first matrix :" ,matrix)

z=np.transpose(matrix)
print("Transpose :",z)


# trace


import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
value = list(map(int, input().split()))

matrix = np.array(value).reshape(a,b)

print("first matrix :" ,matrix)

z=np.trace(matrix)
print("Trace of a matrix : ",z)


# rank



import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
value = list(map(int, input().split()))

matrix = np.array(value).reshape(a,b)

print("first matrix :" ,matrix)

z=np.linalg.matrix_rank(matrix)
print("Rank of a matrix : ",z)


# determinant


import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
value = list(map(int, input().split()))

matrix = np.array(value).reshape(a,b)

print("first matrix :" ,matrix)

z=np.linalg.det(matrix)
print("Determinant of a matrix : ",z)


# inverse


import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
value = list(map(int, input().split()))

matrix = np.array(value).reshape(a,b)

print("first matrix :" ,matrix)

z=np.linalg.inv(matrix)
print("Inverse of a matrix : ",z)


# eigen values and eigen vectors


import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
value = list(map(int, input().split()))

matrix = np.array(value).reshape(a,b)

print("first matrix :" ,matrix)


e1, e2 = np.linalg.eig(matrix)
print("Eigen values : ",e1)
print("eigen vectores :",e2)






