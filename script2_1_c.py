import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import numpy as np
from scipy import interpolate

print(" PUNTO 1.C")


def functionOriginal(num:float):
    return (1/(1+(10*num)**4))

t21 = np.arange(-1, 1, 0.1)
y21= [functionOriginal(item) for item in t21]

#Todo calculate values of splines

tck21 = interpolate.splrep(t21, y21,k=3,s=0)
sol= np.array(interpolate.splev(np.array([-0.95,0.11,0.76]), tck21))
sol= [round(item,5) for item in sol]
print('solucion para splines en valores [-0.95,0.11,0.76]:: ')
print(sol)

#p20_r = np.poly1d(np.polyfit(t21, y21, 20))
p20_r = lagrange(t21, y21)
value= [round(p20_r(e),5) for e in [-0.95,0.11,0.76] ]
print('solucion para poly 20 en valores [-0.95,0.11,0.76]:: ')
print(value)
list_fo21=[functionOriginal(xi) for xi in [-0.95,0.11,0.76] ]
print('solucion para original en valores [-0.95,0.11,0.76]:: ')

print(np.round(list_fo21,5))

# observamos que los polinomios interpolantes estan mas cerca , pero aun asi por la naturaleza del polinomio de la grange
# hya ciertas partes que tienen a desviarse abruptamente cuando llega a los extremos.
#un poco mas ajustado los valores respecto a la funcion original para splines.
lin50 = np.arange(-1,1,0.1)
list21_spline  = np.array(interpolate.splev(lin50, tck21))
list21_poly =p20_r(lin50)


plt.figure()
plt.subplot(211)
plt.plot(lin50,list21_spline, 'bo', color='black',label='splines')
plt.plot(lin50, y21 ,'r--',label='original')
plt.plot(lin50, list21_poly, 'k',color='blue',label='p20')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()

