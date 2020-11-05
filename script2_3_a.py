import numpy as np

def foriginal(xi:float):
    return (np.e**-xi)*np.cos(5*xi)

def fprimax(x:float,h:float):
    solve= (-25 + 48 *foriginal(x+h) - 36*foriginal(x+2*h) + 16*foriginal(x+3*h) -3*foriginal(x+4*h))\
           /(12*h)
    return solve

x=0
I=np.linspace(1,15,15)
list_yi=[]
for n in I:
    h_i= 4**(-n)
    yi=fp_0=fprimax(0,h_i)
    #print("valor para n = : "+ str(n)+" | "  +str(yi))
    print(str(yi))
    list_yi.append(yi)