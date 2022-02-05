import numpy as np
b=np.zeros((2,2,2))
a=np.linspace(1,4,4).reshape(2,2)
b[1,:,:]=a
print(b)
