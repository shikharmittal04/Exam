#Dr Shikhar Mittal, 😃️
#Exam question 4
import numpy as np
import matplotlib.pyplot as plt

n=1024
x=np.zeros(n)

for i in range(n):
	x[i]=np.random.rand()	

fig,ax=plt.subplots(1,2)
ax[0].plot(x,'r.')

FFT=np.fft.fft(x,norm='ortho')
k = 2*np.pi*np.fft.fftfreq(n, d=1)
odr = k.argsort()[::1]
k = k[odr]
FFT = FFT[odr]
print('Min k = ',np.min(k),' and max k = ',np.max(k))
ps=abs(FFT)**2/n

PS=np.zeros(5)
PS[0]=sum(ps[0:204])/204
PS[1]=sum(ps[204:409])/205
PS[2]=sum(ps[409:615])/206
PS[3]=sum(ps[615:820])/205
PS[4]=sum(ps[820:1024])/204

K=np.linspace(np.max(k),np.min(k),6)
K=K+(K[1]-K[0])/2
K=K[0:5]
wid=(np.max(k)-np.min(k))/5
ax[1].bar(K,PS,width=wid)
plt.show()
