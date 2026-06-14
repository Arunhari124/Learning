import numpy as np


array=np.array([[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L']],
               [['M','N','O'],['P','Q','R'],['S','T','U'],['W','V','X']],
               [['s','B','C'],['D','E','F'],['G','K','I'],['J','K','L']]])



#print(array.ndim)


#print(array.shape)
#print(array[0][0][0])


word= array[0,0,0]+ array[2,0,0]
print(word)