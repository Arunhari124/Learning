import numpy as np 

rng=np.random.default_rng()
#print(rng.integers(low=1,high=10,size=3))
#print(np.random.uniform(low=-1,high=1,size=(3,2)))
array=np.array(["apple","bananan","orange",'nigga',"NNN"])
array=rng.choice(array,size=(3,3))
#rng.shuffle(array)
print(array)