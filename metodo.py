import numpy


def inversa(ma):
    return numpy.linalg.inv(ma)

def multMatrizVector(matrix,vect):
    return numpy.matmul(matrix,vect)


def multEscalVector(escal,vect):
    for i in range(len(vect)):
        vect[i]=escal*vect[i]
    return vect

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



