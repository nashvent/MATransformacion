import numpy
import matplotlib.pyplot as plt
from math import *

def inversa(ma):
    return numpy.linalg.inv(ma)

def multMatrizVector(matrix,vect):
    return numpy.matmul(matrix,vect)


def multEscalVector(escal,vect):
    vect2=[]
    for i in range(len(vect)):
        vect2.append(escal*vect[i])
    return vect2

def sumaVector(va,vb):
    vc=[]
    for i in range(len(va)):
        vc.append(va[i]+vb[i])
    return vc


def transformacion(mi,mf,punto):
    invmi=inversa(mi)
    alfaBeta=multMatrizVector(invmi,punto)
    resp=[0]*len(alfaBeta)
    for i in range(len(alfaBeta)):
        tresp=multEscalVector(alfaBeta[i],mf[i])
        resp=sumaVector(resp,tresp)
    return resp


def transformacionLista(mi,mf,puntos):
    npuntos=[]
    for i in range(len(puntos)):
        npuntos.append(transformacion(mi,mf,puntos[i]))
    return npuntos


def parseMathY(formula,xR):
    y=[]
    for x in xR:
        y.append(eval(formula)) 
    return y
def graph(formula,i,f):
    x = numpy.linspace(i,f,100)
    y = parseMathY(formula,x)
    #plt.plot(x, y)   # `r--` for dashed red line
    #plt.show()
    return x,y

