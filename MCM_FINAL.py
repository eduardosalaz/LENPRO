#Programa para encontrar menor comun multiplo


print("Cuantos numeros se utilizaran?")
n=int(input())
while n<1 or n==1:
    print("Tiene que haber mas de un numero")
    print("Cuantos numeros se utilizaran?")
    n=int(input())
a=[]
mcm=[]
mcmSwitch=0
i = 0
while True:
    control = 0
    print("Introduce un numero")
    name=int(input())
    if (name == 0 or name <0):
        print("El numero tiene que ser mayor a uno")
        control = 1
    for j in range (0,i):
        if(name == a[j]):
            print("No se puede introducir un numero mas de una vez")
            control = 1
            break
    if (control == 1):
        i-=1
    elif(control == 0):
        a.append(name)
        mcm.append(name)
    i+=1
    if (i==n):
        break
max=mcm[0]
while True:
      
        for j in range (0,n):
            if (mcm[j]>max):
                max=mcm[j]
        for k in range (0,n):
            if(mcm[k]!=max):
                mcm[k]=mcm[k]+a[k]
        mcmSwitch=0
        for z in range (0,n):
            if(max!=mcm[z]):
                mcmSwitch=1
                break
        if mcmSwitch==0:
            break
print(mcm)
print("El mimimo comun multiplo es " , int(max))