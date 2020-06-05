# Shikhar Mittal
# Exam Question 9
import numpy as np
#np.set_printoptions(precision=3)
#np.set_printoptions(suppress=True)  #NOT in scientific notation

A=np.array([[2,1],[1,0],[0,1]])
B=np.array([[1,1,0],[1,0,1],[0,1,1]])

u, s, vT = np.linalg.svd(A)
print('A=\n',A)
print('Singular values',s,'\n')

u, s, vT = np.linalg.svd(B)
print('B=\n',B)
print('Singular values',s)
