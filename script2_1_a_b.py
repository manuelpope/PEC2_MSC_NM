import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import numpy as np
from scipy import interpolate


print(" PUNTO 1.A")

x = np.array([-1.0 ,-0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
y = np.array([0.00010 ,0.00024, 0.00077,  0.00389, 0.05882 ,1.000000, 0.05882, 0.00389, 0.00077,
             0.00024, 0.00010])
poly = lagrange(x, y)
#print(numpy.polynomial.Polynomial(poly).coef)

print ("-0.95  |",round(poly(-0.95),5))
print (" 0.11  |",round(poly(0.11),5))
print (" 0.76  |",round(poly(0.76),5))

tck = interpolate.splrep(x, y,k=3,s=0)
sol= np.array(interpolate.splev(np.array([-0.95,0.11,0.76]), tck))
sol= [round(item,5) for item in sol]
#print(numpy.polynomial.Polynomial(tck[1]).coef)
print(sol)

# se puede observar que para mayor numero de puntos podemos tener una
# mejor aprox por lagrange debido a que se ajusta mejor a los valores, por
# eso la aprox de spline no puede interpolar y sus resultados pueden llegar a estar
# completamente defasados.

print(" PUNTO 1.B")

def functionOriginal(num:float):
    return (1/(1+(10*num)**4))
linspace= np.linspace(-1,1,11)
list_v= [functionOriginal(item) for item in [-0.95,0.11,0.76]]
list_v=np.array(list_v)

def errorRelativo(x:list,y:list):
    n= len(x)
    result=[]
    for i in range(n):
        print("original: "+ str(x[i]) + ' | '+ 'interpolacion: '+ str(y[i]))
        result.append(100*(abs(x[i]-y[i]))/y[i])

    return result


print(errorRelativo(list_v,sol))

p10_r = np.poly1d(np.polyfit(x, y, 10))
value= p10_r([-0.95,0.11,0.76])
print(value)


# evenly sampled time at 200ms intervals
t = np.arange(-1, 1, 0.2)
listfo= [functionOriginal(item) for item in t]
listp10= [p10_r(item) for item in t]
list_pl= interpolate.splev(np.array(t), tck)




# red dashes, blue squares and green triangles

plt.figure()
plt.subplot(211)
plt.plot(t,list_pl, 'bo', color='black',label='splines')
plt.plot(t, listfo ,'r--',label='original')
plt.plot(t, listp10, 'k',color='blue',label='p10')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
#plt.show()



