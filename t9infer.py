from t9functions import readTextFile
from t9functions import getNMatrix
import numpy

filename = "47537.txt"
text = readTextFile(filename)

#subText = text[1:400]
#print(subText)

N, sp = getNMatrix(text)
print(numpy.sum(N))

