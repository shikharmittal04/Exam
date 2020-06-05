#Shikhar Mittal
#Exam question 10
#We can either change the range of x or the no.of points. I have changed the latter.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

def rect(x):
    return np.where(abs(x)<=1,1,0)

x_min=-10
x_max=10
fig,ax=plt.subplots(1,2)

for N in [64,128,256]:	
	x=np.linspace(x_min,x_max,N)
	Dx=x[1]-x[0]
	fx=rect(x)

	FTfx=np.fft.fft(fx,norm='ortho')
	k1 = 2*np.pi* np.fft.fftfreq(N, d=Dx)
	FTfx=Dx*np.exp(-1j*k1*x_min)*FTfx*np.sqrt(N/2/np.pi)

	ax[0].plot(x,fx,color=(0.0,0.0,N/256.0))
	
	odr = k1.argsort()[::1]
	k1 = k1[odr]
	FTfx = FTfx[odr]

	ax[1].plot(k1,np.real(FTfx),color=(N/256.0,0.0,0.0))
	

ax[0].set_xlabel(r'$x$',fontsize=16)
ax[0].set_ylabel(r'$f(x)$',fontsize=16)
ax[0].set_title('Function',fontsize=16)
ax[0].grid(True)
ax[1].set_xlabel(r'$k$',fontsize=16)
ax[1].set_ylabel(r'$\tilde{f}(k)$',fontsize=16)
ax[1].set_title('Fourier transform',fontsize=16)
ax[1].grid(True)
plt.show()
