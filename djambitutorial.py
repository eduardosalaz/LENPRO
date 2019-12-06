import os
clear = lambda: os.system('cls')

'''
MMN
RPM
LAM
 
112
341
561
 
1 = Militante
2 = Necromovil
3 = Reportero
4 = Provocador
5 = Lider
6 = Asesino
 
 
 
 
'''
'''
Inicio del menu
'''
print("     Bienvenido a Djambi.\n")
print(r"""
____   _                 _     _ 
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/                         

""")
input("\nPresione la tecla intro para continuar...")
clear()

tablero=[]
 
for y in range (0,11):
      
   tablero.append([00]*11)

#coordenadas
tablero[0][0]=0
tablero[0][1]=1
tablero[0][2]=2
tablero[0][3]=3
tablero[0][4]=4
tablero[0][5]=5
tablero[0][6]=6
tablero[0][7]=7
tablero[0][8]=8
tablero[0][9]=9


tablero[1][0]=1
tablero[2][0]=2
tablero[3][0]=3
tablero[4][0]=4
tablero[5][0]=5
tablero[6][0]=6
tablero[7][0]=7
tablero[8][0]=8
tablero[9][0]=9

      
#Piezas jugador 1
tablero[1][1]=511
tablero[1][2]=611  
tablero[1][3]=111
tablero[2][1]=311
tablero[2][2]=411
tablero[2][3]=111
tablero[3][1]=111
tablero[3][2]=111
tablero[3][3]=211
 
#Piezas jugador 2
tablero[1][7]=121
tablero[1][8]=621  
tablero[1][9]=521
tablero[2][7]=121
tablero[2][8]=421
tablero[2][9]=321
tablero[3][7]=221
tablero[3][8]=121
tablero[3][9]=121
 
#Piezas jugador 3
tablero[7][1]=131
tablero[7][2]=131
tablero[7][3]=231
tablero[8][1]=331
tablero[8][2]=431
tablero[8][3]=131
tablero[9][1]=531
tablero[9][2]=631
tablero[9][3]=131
 
#Piezas jugador 4
tablero[7][7]=241
tablero[7][8]=141
tablero[7][9]=141
tablero[8][7]=141
tablero[8][8]=441
tablero[8][9]=341
tablero[9][7]=141
tablero[9][8]=641
tablero[9][9]=541
#MOVIMIENTO DE MILITANTE
print(r"""
____   _                 _     _ 
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/                         

""")
print("Objetivo: \nCapturar a los demás líderes enemigos con el uso de las diferentes piezas o estrategias entre jugadores como alianzas de manera informal. \n")
print("Movimientos del djambi: \nCada jugador moverá una pieza en su turno, con la posibilidad de capturar en este movimiento a una ficha contraria. \n")
clear()
print("La letra M en el tablero Representa a los Militantes.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==1):
            if (color==1 and status==1 and x ==1):
                print("\033[1;34;40m M", end ="")
            elif (color==1 and status==1 and x !=1):
                print("\033[1;37;40m 0", end ="")
            elif(color==2 and status==1):
                print ("\033[1;37;40m 0", end ="")
            elif(color==3 and status==1):
                print ("\033[1;37;40m 0", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;37;40m 0", end ="")
            elif(status==0):
                print ("\033[1;35;40m M", end ="")  
        elif(x==1 and ((y<3 and y>0) or y>3)):   
            print("\033[1;36;40m 0", end="")
        elif(y==3 and x>1):   
            print("\033[1;36;40m 0", end="") 
                     
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=1 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\n")
input("Presione la tecla intro para continuar...")
clear()
#MOVIMIENTO DE LIDER
print(r"""
____   _                 _     _ 
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/                         

""")
print("La letra L en el tablero Representa a los lideres.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==5):
            if (color==1 and status==1):
                print("\033[1;34;40m L", end ="")
            elif(color==2 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(color==3 and status==1):
                print ("\033[1;36;40m 0", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(status==0):
                print ("\033[1;37;40m 0", end ="")
        elif(x==1 and y>1 and y<10):   
            print("\033[1;36;40m 0", end="")
        elif(y==1 and x>1 and x<10):   
            print("\033[1;36;40m 0", end="") 
        elif(x==y and x>1):
            print("\033[1;36;40m 0", end="")                 
        elif (x==5 and y==5):
            print ("\033[1;36;40m ", end="")
        elif (pieza!=5 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\n")
input("\033[1;37;40mPresione la tecla intro para continuar...")
clear()
#MOVIMIENTO DE ASESINO
print(r"""
____   _                 _     _ 
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/                         

""")
print("La letra A en el tablero Representa a los Asesinos.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==6):
            if (color==1 and status==1):
                print("\033[1;34;40m A", end ="")
            elif(color==2 and status==1):
                print ("\033[1;31;40m A", end ="")
            elif(color==3 and status==1):
                print ("\033[1;33;40m A", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;32;40m A", end ="")
            elif(status==0):
                print ("\033[1;35;40m A", end ="")    
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=6 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\n")
input("Presione la tecla intro para continuar...")
clear()
#MOVIMIENTO DE NECROMÓVIL
print(r"""
____   _                 _     _ 
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/                         

""")
print("La letra N en el tablero Representa a los Necromóviles.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==2):
            if (color==1 and status==1):
                print("\033[1;34;40m N", end ="")
            elif(color==2 and status==1):
                print ("\033[1;31;40m N", end ="")
            elif(color==3 and status==1):
                print ("\033[1;33;40m N", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;32;40m N", end ="")
            elif(status==0):
                print ("\033[1;35;40m N", end ="")    
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=2 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\n")
input("Presione la tecla intro para continuar...")
clear()
#MOVIMIENTO DE reportero
print(r"""
____   _                 _     _ 
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/                         

""")
print("La letra R en el tablero Representa a los Reporteros.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==3):
            if (color==1 and status==1):
                print("\033[1;34;40m R", end ="")
            elif(color==2 and status==1):
                print ("\033[1;31;40m R", end ="")
            elif(color==3 and status==1):
                print ("\033[1;33;40m R", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;32;40m R", end ="")
            elif(status==0):
                print ("\033[1;35;40m R", end ="")    
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=3 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\n")
input("Presione la tecla intro para continuar...")
clear()
#MOVIMIENTO DE provocador
print(r"""
____   _                 _     _ 
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/                         

""")
print("La letra P en el tablero Representa a los Provocadores.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==4):
            if (color==1 and status==1):
                print("\033[1;34;40m P", end ="")
            elif(color==2 and status==1):
                print ("\033[1;31;40m P", end ="")
            elif(color==3 and status==1):
                print ("\033[1;33;40m P", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;32;40m P", end ="")
            elif(status==0):
                print ("\033[1;35;40m P", end ="")    
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=4 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\n")
input("Presione la tecla intro para continuar...")