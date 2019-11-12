print("Suma y multiplicacion de matrices")
decision=int(input("Para sumar matrices ingresa 1, para multiplicar ingresa 2"))
if decision== 1:
    na = int(input("Ingresar numero de columnas de la matriz A"))
    ma= int(input("Ingresar numero de filas de la matriz A"))
    print(na,ma)
    matrizA = []
    for i in range(0,ma):
        matrizA.append([])
        for j in range(0,na):
            matrizA[i].append(0)
            matrizA[i][j] = int(input())
    print("Matriz A")        
    for a in matrizA:
        print (a)
    nb = int(input("Ingresar numero de columnas de la matriz B"))
    mb= int(input("Ingresar numero de filas de la matriz B"))
    print(nb,mb)
    matrizB = []
    for i in range(0,mb):
        matrizB.append([])
        for j in range(0,nb):
            matrizB[i].append(0)
            matrizB[i][j] = int(input())
    print ("Matriz B")
    for b in matrizB:
        print (b)
    if na == nb and ma == mb:
        matrizC = []
        for i in range(len(matrizA)):
            matrizC.append([])
            for j in range(len(matrizB[0])):
                matrizC[i].append(0) 
                matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
        print ("Matriz C")
        for c in matrizC:
            print(c)
    else:
        print ("El numero de filas y columnas no es valido")
elif decision == 2:
    na = int(input("Ingresar numero de columnas de la matriz A"))
    ma= int(input("Ingresar numero de filas de la matriz A"))
    print(na,ma)
    matrizA = []
    for i in range(0,ma):
        matrizA.append([])
        for j in range(0,na):
            matrizA[i].append(0)
            matrizA[i][j] = int(input())
    print("Matriz A")        
    for a in matrizA:
        print (a)
    nb = int(input("Ingresar numero de columnas de la matriz B"))
    mb= int(input("Ingresar numero de filas de la matriz B"))
    print(nb,mb)
    matrizB = []
    for i in range(0,mb):
        matrizB.append([])
        for j in range(0,nb):
            matrizB[i].append(0)
            matrizB[i][j] = int(input())
    print ("Matriz B")
    for b in matrizB:
        print (b)
    if na == mb:
        matrizC = []  
        for i in range(len(matrizA)):
            matrizC.append([]) 
            for j in range(len(matrizA[0])):
                matrizC[i].append(0) 
                for k in range(len(matrizB)): 
                    matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
        print("Matriz C")
        for c in matrizC:
            print(c)
    else:
        print("El numero de filas y columnas no es valido")
else:
    print("Ingresar una operacion valida")