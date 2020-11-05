import numpy as np
import matplotlib.pyplot as plt

print('PUNTO 2.A')

def orginalfunction(xi:float):
    return ((1+xi**2)**-1)

print(' listas para 2 , 4, 10, 20 grados')

list2= [orginalfunction(elem) for elem in np.linspace(-3,3,3)]
list4= [orginalfunction(elem) for elem in np.linspace(-3,3,5)]
list10= [orginalfunction(elem) for elem in np.linspace(-3,3,11)]
list20= [orginalfunction(elem) for elem in np.linspace(-3,3,21)]

p2_r = np.poly1d(np.polyfit(np.linspace(-3,3,3), list2, 2))
p4_r = np.poly1d(np.polyfit(np.linspace(-3,3,5), list4, 4))
p10_r = np.poly1d(np.polyfit(np.linspace(-3,3,11), list10, 10))
p20_r = np.poly1d(np.polyfit(np.linspace(-3,3,21), list20, 20))

t= np.linspace(-3,3,20)
val_o= [orginalfunction(elem) for elem in t]
plt.figure()
plt.subplot(211)
plt.plot(t,p20_r(t), 'k--', color='black',label='p20')
plt.plot(t, p2_r(t) ,'r--',label='p2')
plt.plot(t, p10_r(t), 'k-*',color='green',label='p10')
plt.plot(t, p4_r(t), 'k-',color='purple',label='p4')


plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

plt.subplot(212)
plt.plot(t, val_o ,'r--',label='original')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.2)



plt.show()


#en este caso se obersva que la p20 es la que mejor ajusta  a nuestra grafica ,
#describe mejor su trayectoria  y si aplicamos el rms sera menor que las otras
#p10 tiene un buen comportamiento en la zona central pero a los puntos extremos
#tiene algunos saltos que lo sacan totalmente del valor a predecir real.

