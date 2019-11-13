n = int(input("1.- Array de 3x3 2.- Array de 4x4 3.- Array de 5x5"))
newarray = []
resultado = []
if n==1:
        n=3
elif n==2:
        n=4
elif n==3:
        n=5
    
        
        
for i in range(n):
        
    newarray.append([0]*n)

for i in range(0,n):
    for j in range(0,n):
        newarray[i][j]=int(input("Ingrese el valor"))
        
    resultado.append(int(input("ingrese el resultado")))
    
if n==3:
            
          
    #pivote 1
    PA = newarray[0][0]
            
            
    newarray[1][1] = ((newarray[0][0])*(newarray[1][1])-(newarray[1][0])*(newarray[0][1]))/1;
    newarray[1][2]= ((newarray[0][0])*(newarray[1][2])-(newarray[1][0])*(newarray[0][2]))/1;
    resultado[1]= ((newarray[0][0])*(resultado[1])-(newarray[1][0])*(resultado[0]))/1;
        
    newarray[2][1]= ((newarray[0][0])*(newarray[2][1])-(newarray[2][0])*(newarray[0][1]))/1
    newarray[2][2]= ((newarray[0][0])*(newarray[2][2])-(newarray[2][0])*(newarray[0][2]))/1
    resultado[2]= ((newarray[0][0])*(resultado[2])-(newarray[2][0])*(resultado[0]))/1
        
    newarray[1][0] = 0
    newarray[2][0] = 0
    #pivote 2
    newarray[0][0]= ((newarray[1][1])*(newarray[0][0])-(newarray[0][1])*(newarray[1][0]))/PA
    newarray[0][2]= ((newarray[1][1])*(newarray[0][2])-(newarray[0][1])*(newarray[1][2]))/PA
    resultado[0]= ((newarray[1][1])*(resultado[0])-(newarray[0][1])*(resultado[1]))/PA
        
    newarray[2][2]= ((newarray[1][1])*(newarray[2][2])-(newarray[2][1])*(newarray[1][2]))/PA
    resultado[2]= ((newarray[1][1])*(resultado[2])-(newarray[2][1])*(resultado[1]))/PA      
        
    newarray[0][1] = 0
    newarray[2][1] = 0
        
    PA = newarray[1][1]
    #pivote 3
        
    newarray[0][0]= (int((newarray[2][2])*(newarray[0][0])-(newarray[0][2])*(newarray[2][0]))/PA)
    resultado[0]= ((newarray[2][2])*(resultado[0])-(newarray[0][2])*(resultado[2]))/PA
        
    newarray[1][1]= ((newarray[2][2])*(newarray[1][1])-(newarray[1][2])*(newarray[2][1]))/PA
    resultado[1]= ((newarray[2][2])*(resultado[1])-(newarray[1][2])*(resultado[2]))/PA      
                
    newarray[0][2] = 0
    newarray[1][2] = 0  
        
    #Resultado
    resultado[0] = resultado[0]/newarray[0][0]
    resultado[1] = resultado[1]/newarray[1][1]
    resultado[2] = resultado[2]/newarray[2][2]
    
print(resultado[0])
print(resultado[1])
print(resultado[2])