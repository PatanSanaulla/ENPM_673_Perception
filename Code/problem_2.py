import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

#reading the file name form the command arguments
csvFileName = sys.argv[1]+'.csv'

datadict = {}
with open(csvFileName) as csvfile:
	data = csv.reader(csvfile, delimiter = ',')
	for row in data:
		datadict[row[0]] = row[1]

#Creating a matrix of each type to further compute
matrix_y = []
matrix_x = []
for i in datadict:
	try:
		matrix_y.append(float(datadict[i]))
		matrix_x.append([float(i)*float(i), float(i), 1])
	except ValueError:
		#The value found is not a float
		continue

y = np.array(matrix_y)
x = np.array(matrix_x)

xt = np.transpose(x)

one = np.linalg.inv(np.matmul(xt, x))
two = np.matmul(xt, y)

B = np.matmul(one, two)

#plotting the curve based on the generated values form B
yi = []
xcoords = []
for xi in x:
	yi.append(xi[0]*B[0] + xi[1]*B[1] + xi[2]*B[2])
	xcoords.append(xi[1])

plt.plot(xcoords, matrix_y, 'bo')
plt.plot(xcoords, yi, 'ro')
plt.show()