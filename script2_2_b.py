from numpy.polynomial import chebyshev
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import numpy as np
from scipy import interpolate


coeffs_cheb = [0] * 11 + [1]  # Solo queremos el elemento 11 de la serie
T10 = chebyshev.Chebyshev(coeffs_cheb, [-3, 3])
xp_ch_10 = T10.roots()
print(xp_ch_10)

coeffs_cheb = [0] * 21 + [1]  # Solo queremos el elemento 11 de la serie
T21 = chebyshev.Chebyshev(coeffs_cheb, [-3, 3])
xp_ch_21 = T21.roots()
print(xp_ch_21)



def orginalfunction(xi:float):
    return ((1+xi**2)**-1)


listO10=[orginalfunction(elem) for elem in xp_ch_10]
listO20=[orginalfunction(elem) for elem in xp_ch_21]


p10_r = np.poly1d(np.polyfit(xp_ch_10, listO10, 10))
p20_r = np.poly1d(np.polyfit(xp_ch_21, listO20, 20))

t= np.linspace(-3,3,50)
val_o= [orginalfunction(elem) for elem in t]
plt.figure()
plt.subplot(211)
plt.plot(t,p20_r(t), 'k--', color='black',label='p20')
plt.plot(t, p10_r(t), 'k-*',color='green',label='p10')
plt.plot(t, val_o ,'r--',label='original')



plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

plt.subplot(212)
plt.plot(t, val_o ,'r--',label='original')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.2)



plt.show()

#asombrosa reduccion del error cuando se le aplica los nodos adecuados
#el realizar esta interpolacion en chevyshev reduce notablemente
#los problemas en los extremos y ademas con polinomios de menor
#orden se cosniguen grandes avances.