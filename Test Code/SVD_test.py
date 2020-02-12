import numpy as np 
import math
from numpy import linalg as LA

# First entry in list set as None for more intuitive indexing
x = [None, 5, 150, 150, 5]
y = [None, 5, 5, 150, 150]
xp = [None, 100, 200, 220, 100]
yp = [None, 100, 80, 80, 200]

A = np.array([[-x[1], -y[1], -1, 0, 0, 0, x[1]*xp[1], y[1]*xp[1], xp[1]], 
	[0, 0, 0, -x[1], -y[1], -1, x[1]*yp[1], y[1]*yp[1], yp[1]], 
	[-x[2], -y[2], -1, 0, 0, 0, x[2]*xp[2], y[2]*xp[2], xp[2]], 
	[0, 0, 0, -x[2], -y[2], -1, x[2]*yp[2], y[2]*yp[2], yp[2]], 
	[-x[3], -y[3], -1, 0, 0, 0, x[3]*xp[3], y[3]*xp[3], xp[3]], 
	[0, 0, 0, -x[3], -y[3], -1, x[3]*yp[3], y[3]*yp[3], yp[3]], 
	[-x[4], -y[4], -1, 0, 0, 0, x[4]*xp[4], y[4]*xp[4], xp[4]], 
	[0, 0, 0, -x[4], -y[4], -1, x[4]*yp[4], y[4]*yp[4], yp[4]]])

print(A)

A_transpose = np.transpose(A)

# intermediate_matrix = c_transpose * c
# intermediate_matrix = np.multiply(c_transpose,c)   #does the dot product
intermediate_matrix = np.matmul(A_transpose,A)

# print(f'C transpose:\n {c_transpose}')

# print(f'Intermediate matrix:\n {intermediate_matrix}')

# eigen_value_matrix = np.diag((1, 2, 3))
# print(diagonal_test)

w, v = LA.eig(intermediate_matrix)
# print(w) #Eigen values
# print(v) #Eigen vector matrix

V_eigen_vector_matrix = v
V_transpose = np.transpose(V_eigen_vector_matrix)

eigen_square_root = []
# print(w[1])

for i in range(0,len(w)):
	eigen_square_root.append(math.sqrt(abs(w[i])))

# print(eigen_square_root)

Sigma_eigen_value_matrix = np.diag(eigen_square_root)

# print(Sigma_eigen_value_matrix)
# print(math.sqrt(4)) 

Sigma_inverse = np.linalg.inv(Sigma_eigen_value_matrix)

U_matrix = np.matmul(A, np.matmul(V_eigen_vector_matrix,Sigma_inverse))

print(f'SVD decomposition of C is:\nU: \n {U_matrix}')	
print(f'Sigma :\n {Sigma_eigen_value_matrix}')	
print(f'V transpose :\n {V_transpose}')

SVD_check = np.matmul(U_matrix, np.matmul(Sigma_eigen_value_matrix, V_transpose))
print(f'SVD check matrix:\n {SVD_check}')

# if A==SVD_check:
# 	print('SVD successful')















