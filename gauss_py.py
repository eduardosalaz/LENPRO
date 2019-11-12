import copy
from fractions import Fraction
def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det
 
        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]
 
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b
def matcero(p, q):
    return [[0]*q for i in range(p)]
def matmul(a, b):
    n, p = len(a), len(a[0])
    p1, q = len(b), len(b[0])
    if p != p1:
        raise ValueError("Dimensiones incompatibles")
    c = matcero(n, q)
    for i in range(n):
        for j in range(q):
                c[i][j] = sum(a[i][k]*b[k][j] for k in range(p))
    return c
def mapmat(f, a):
    return [list(map(f, v)) for v in a]
def ratmat(a):
    return mapmat(Fraction, a)
print("Sistemas de ecuaciones de 3 a 5 variables")
print("Resolver sistema de ecuaciones de 3 a 5 variables")
filas = int(input("Ingresar el numero de variables del sistema: "))
if filas >= 3 and filas <= 5:
    columnas = filas    
    a = []
    print("Ingresar los coeficientes del sistema")
    for i in range(0,filas):
        a.append([])
        for j in range(0,filas):
            a[i].append(0)
            a[i][j] = int(input())
    print("Matriz de coeficientes es")
    print(end="")
    for display in a:
        print(display)
    print("Ingresar las soluciones de las ecuaciones")
    b = []
    for i in range(0,columnas):
        b.append([])
        for j in range(0,1):
            b[i].append(0)
            b[i][j] = int(input())
    print("Matriz de soluciones es")
    print(b)
    print(end="")
    det, c = gauss(a, b)
    print("Las soluciones al sistema son:")
    print (c)
    c
else:
    print("Ingresar un numero de variables valido") 
k = input("Ingresar enter para salir")
