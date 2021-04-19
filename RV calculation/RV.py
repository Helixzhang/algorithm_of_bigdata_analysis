import numpy as np

A = np.matrix([[1,2,3],[2,3,4]])
# print(np.trace(A*A.I))

def RV(martrixA,martrixB):
    # return np.trace(martrixA*martrixA.I*martrixB*martrixB.I)/np.sqrt(np.trace(np.power(martrixA*martrixA.I,2))*np.trace(np.power(martrixB*martrixB.I,2)))
    return np.trace((martrixA.I*martrixB)*(martrixB.I*martrixA))/np.sqrt(np.trace(np.power(martrixA.I*martrixA,2))*np.trace(np.power(martrixB.I*martrixB,2)))

print(RV(np.matrix([[4,0,6,0],[0,0,0,1]]),np.matrix([[1,1,1],[1,1,1]])))