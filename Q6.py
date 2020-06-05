#Shikhar Mittal
#Exam: Question 6

def f(x,y):
	return np.array([32*y[0]+66*y[1]+2*x/3+2/3,-66*y[0]-133*y[1]-x/3-1/3])
	
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scint

Sol=scint.solve_ivp(f, [0, 0.5], [1/3,1/3],t_eval=np.linspace(0,0.5,50))

x=np.linspace(0,0.5,100)
y1=(2*np.exp(-x)-np.exp(-100*x)+2*x)/3	#I worked out the analytical
y2=(-np.exp(-x)+2*np.exp(-100*x)-x)/3	#solution.

plt.plot(Sol.t,Sol.y[0],'b',x,y1,'b--')
plt.plot(Sol.t,Sol.y[1],'r',x,y2,'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['$y_1$','$y_1$ analytical','$y_2$','$y_2$ analytical'])
plt.grid(True)
plt.show()

#The overlap is perfect hence the difference may not be visible!
