import numpy as np


scores=np.array([91,55,100,73,82,64])

scores[scores < 60] = 0

print(scores)