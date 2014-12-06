from t9functions import readTextFile

filename = "47537.txt"
text = readTextFile(filename)
subText = text[1:400]
print(subText)
