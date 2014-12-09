from t9functions import readTextFile
from t9functions import getNandRMatrix
from t9functions import getQMatrix
import numpy

filename = "47537.txt"
text = readTextFile(filename)

#subText = text[1:400]
#print(subText)


N, R = getNandRMatrix(text)
P = N
#print(numpy.sum(N))
Q = getQMatrix()
#print(Q)
#Rows
##print("Sum of the rows of P = ")
##print(numpy.sum(N, axis=0))
##
##print("Sum of the rows of Q = ")
##print(numpy.sum(Q, axis=0))
##
##print("Sum of the rows of R = ")
##print(numpy.sum(R, axis=0))
##
##print("Sum over the columns of P = ")
##print(numpy.sum(P, axis=1))
##
##print("Sum over the columns of Q = ")
##print(numpy.sum(Q, axis=1))
##
##print("Sum over the columns of R = ")
##print(numpy.sum(R, axis=1))
##
