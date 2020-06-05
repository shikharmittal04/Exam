#Shikhar Mittal
#Exam Question 8
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scint

def fun(x, y):
	return np.vstack(( y[1], 4*(y[0]-x) ))

def BC(ya, yb):
	return np.array([ya[0], yb[0]-2])

x = np.linspace(0, 1,20)
y_int = np.zeros((2, x.size))
Sol = scint.solve_bvp(fun, BC, x, y_int)
y1 = np.sinh(2*x)/np.sinh(2)+x
plt.plot(x,Sol.sol(x)[0],'b',x,y1,'r.')

Err=(y1-Sol.sol(x)[0])/y1*100
print('Relative error %\n')
for e in Err:
	print(e)
	
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.show()
