DIAN=int(input("Dia de nacimiento : ")) 
MESN=int(input("Mes de nacimiento (numero) : ")) 
AÑON=int(input("Dia de nacimiento (4 digitos) : ")) 

DIAA=int(input("Dia Actual : ")) 
MESA=int(input("Mes Actual (numero) : ")) 
AÑOA=int(input("Dia Actual (4 digitos) : ")) 

while True :
    
    if AÑOA % 4 = 0:
        #Es bisiesto
        bisiesto=1
    #Cuando el dia llegue a 0 se baja un valor de mes
    if  DIAA<1:
        MESA=MESA-1
    #Cuando el mes llegue a 0 se baja un valor de mes
    if MESA<1:
        AÑOA=AÑOA-1
    #Cuando sea mes de 31 dias    
    if MESA = 1 or 3 or 5 or 7 or 8 or 10 or 12:
        DIAA=31
    #Cuando sea mes de 30 dias
    if MESA=4 or 6 or 9 or 11:
        DIAA=30
    #Febrero cuando sea mes bisiesto    
    if MESA= 2 and bisiesto=1
        DIAA=29
    #Febrero cuando no sea mes bisiesto
    if MESA= 2 and bisiesto=0
        DIAA=28
        
 
        
    
    #Cuando lleguemos al limite
    if DIAN=DIAA and MESA=MESN and AÑON=AÑOA:
        break
    
print(Dias)    
