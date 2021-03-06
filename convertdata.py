import numpy as np

filename = 'data_set.txt'
fileObj = open(filename, "r")
words = fileObj.read().splitlines()
fileObj.close
macaddres = np.char.split(words)

lastlength = len(macaddres[5])-1
lastlength2 = len(macaddres[10])-1
      

print(macaddres[5][lastlength])
print(macaddres[10][lastlength2])

