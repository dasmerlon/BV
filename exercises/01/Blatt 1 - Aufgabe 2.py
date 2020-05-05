# -*- coding: utf-8 -*-

import numpy as np

u = np.zeros((1,100))
v = np.array([0,1,2,3,4,5,6,7,8,9,10,11])

m = v.reshape(3,4)

m = m * 1.2
m = m.astype(int)
m = m * 1.2 # wird zu einem float64

m = m * m    #multiplikationen mit matrizen ist schon elementweise
print(m)