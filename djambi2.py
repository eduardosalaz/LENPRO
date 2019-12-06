import os
clear = lambda: os.system('cls')
vertical=0
horizontal=0
diagonal=0
cs=0
turnos = 1
terminar = 0
poder=0
contadorpoder=0
contadorturnos=1
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
print("     Bienvenido a Djambi.")
input("Presione la tecla intro para continuar...")
clear()






'''
Aqui empieze la impresion del tablero
'''

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
'''
Reglamento 
'''
print("REGLAMENTO\n")
print("El objetivo del juego es ser el último líder en pie.\n")
print("Cada jugador mueve en su turno una de sus fichas pudiendo capturar una pieza adversaria o solo moverse a una casilla vacía.\n")
print("Cuando un jugador mueve una pieza no puede saltar por encima de las demás piezas aliadas o adversarias.\n")
print("Para capturar una pieza, se debe posicionar exactamente encima de la posición de dicha pieza a ser capturada, sin pasarse de casilla, con algunas excepciones.\n")
print("Cuando un jugador captura una pieza enemiga puede moverla a una casilla vacía distinta a la casilla central, con algunas excepciones.\n")
print("La casilla central solo puede estar ocupada por una pieza de tipo líder.\n")
print("Cuando el líder de un equipo se encuentra en la casilla central, tiene derecho a un turno extra después de los turnos de los demás jugadores.\n")
print("Líder: Puede moverse de manera horizontal, vertical o diagonal con un máximo de 8 casillas.\n")
print("Militantes: Pueden moverse de manera horizontal, vertical o diagonal con un máximo de 2 casillas.\n")
print("Asesino: Puede moverse de  manera horizontal, vertical o diagonal con un máximo de 8 casillas.\nCuando captura a una pieza, se ve obligado a mover dicha pieza capturada a la casilla de la posición original del asesino.\n")
print("Reportero: Puede moverse de manera horizontal, vertical o diagonal con un máximo de 8 casillas.\nPara capturar a una pieza, debe de colocarse en una casilla adyacente de manera horizontal o vertical, no diagonal.\n")
print("El provocador y necromóvil son las únicas 2 piezas que no pueden matar otras, pero transportan piezas enemigas vivas o capturadas.\n")
print("Provocador: Puede moverse de manera horizontal, vertical o diagonal con un máximo de 8 casillas.\nEsta pieza no puede capturar piezas contrarias, pero puede mover piezas vivas, de una manera similar a la captura.\n")
print("Necromóvil: Puede moverse de manera horizontal, vertical o diagonal con un máximo de 8 casillas.\nEsta pieza no puede capturar piezas contrarias, pero puede mover piezas previamente capturadas, de una manera similar a la captura.\n")
print("\n")
input("\033[1;37;40m Presione la tecla intro para iniciar el juego...")
def actualizar():
    clear()
    print("L = Líder. M = Militante. A = Asesino. R = Reportero. P = Provocador. N = Necromóvil.   Solo se pueden ingresar numeros enteros del 1 al 9\n")
    
    for x in range (0,10):
       for y in range (0,10):
           pieza=int(tablero[x][y]/100)   
           color=int((tablero[x][y]%100)/10)
           status=int(tablero[x][y]%10)
           if (pieza==1):
               if (color==1 and status==1):
                   print("\033[1;34;40m M", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;31;40m M", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m M", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m M", end ="")
               elif(status==0):
                   print ("\033[1;35;40m M", end ="")    
              
           elif (pieza==2):
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
           elif (pieza==3):
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
           elif (pieza==4):
               if (color==1):
                   print("\033[1;34;40m P", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;31;40m P", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m P", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m P", end ="")
               elif(status==0):
                   print ("\033[1;35;40m P", end ="")    
           elif (pieza==5):
               if (color==1 and status==1):
                   print("\033[1;34;40m L", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;31;40m L", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m L", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m L", end ="")
               elif(status==0):
                   print ("\033[1;35;40m L", end ="")    
           elif (pieza==6):
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
               print ("\033[1;36;40m",tablero[x][y], end="")
           elif (pieza==0 and pieza!=10 ):
               print ("\033[1;37;40m",tablero[x][y], end="")
           elif(pieza==10):
               print ("\033[1;37;40m 0", end="")
              
       print("\n")
    if(turnos==1):
      print("\033[1;34;40m Equipo ",turnos)
    elif(turnos==2):
      print("\033[1;31;40m Equipo ",turnos)
    elif(turnos==3):
      print("\033[1;33;40m Equipo ",turnos)
    elif(turnos==4):
      print("\033[1;32;40m Equipo ",turnos)


while(terminar == 0):
    #checar que ningue rey este encerrado por piezas capturadas y no tenga necromovil
    for x in range (0,10):
       for y in range (0,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          if(color==1 and pieza==5):
             rey1=tablero[x][y]
             
          if(color==2 and pieza==5):
             rey2=tablero[x][y]
             
          if(color==3 and pieza==5):
             rey3=tablero[x][y]
             
          if(color==4 and pieza==5):
             rey4=tablero[x][y]
    #checar si el rey esta vivo para turnos         
    actualizar()
    for x in range (0,10):
       for y in range (0,10):
           pieza=int(tablero[x][y]/100)   
           color=int((tablero[x][y]%100)/10)
           status=int(tablero[x][y]%10)
           if (pieza==5 and color==1):
              sr1=status
           if (pieza==5 and color==2):
              sr2=status
           if (pieza==5 and color==3):
              sr3=status
           if (pieza==5 and color==4):
              sr4=status    
    '''
    Aqui empieza turnos
    '''
    
    if (turnos == 1 and sr1==1):
        reiniciar = 0
        
        while(reiniciar == 0):
            reiniciar = 1
            while True:
               while True:
                  try:
                     inicio = int(input("\033[1;37;40m¿Qué pieza desea mover? (fila)   ."))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(inicio<10 and inicio>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     inicio2 = int(input("\033[1;37;40m¿Qué pieza desea mover? (columna)  ."))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
                     
               if(inicio2<10 and inicio2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            
            if(tablero[inicio][inicio2]== 0):
              print("No hay pieza en ese lugar.")
              reiniciar = 0
            if(tablero[inicio][inicio2]%10==10):
               print("No puedes seleccionar piezas capturadas.")
               reiniciar=0
            if((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (tablero[inicio+1][inicio2-1]==0 and inicio2-1>0 and inicio+1<10) or (tablero[inicio+1][inicio2]==0 and inicio+1<10) or (tablero[inicio+1][inicio2+1]==0 and inicio2+1<10 and inicio+1<10) or (tablero[inicio][inicio2+1]==0 and  inicio2+1<10) or (tablero[inicio-1][inicio2+1]==0 and  inicio2+1<10 and inicio-1>0)):
               print(" ",end="")
            else:   
               print("No puedes escoger una pieza encerrada.")
               reiniciar=0
              
            
            
            if(((tablero[inicio][inicio2]%100)/10 != turnos + 0.1) and tablero[inicio][inicio2]!= 0 ):
               print("Esa pieza no es de tu equipo.")
               reiniciar = 0
            
              
               
                
        while (reiniciar==1):
            reiniciar = 0
            while True:
               while True:
                  try:
                     final = int(input("¿A dónde la quiere mover? (fila)   ."))
                     break
                  except ValueError:
                     print("Sólo numeros enteros entre 1 y 9.")
               if(final<10 and final>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     final2 = int(input("¿A dónde la quiere mover? (columna)   ."))
                     break
                  except ValueError:
                     print("Sólo numeros enteros entre 1 y 9.")
               if(final2<10 and final2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")

            if(tablero[final][final2] == tablero[inicio][inicio2] and tablero[final][final2] != 0 ):
                print("No se puede mover al mismo lugar.")
                reiniciar = 1
            if(int(tablero[inicio][inicio2]/100)!=5 and final==5 and final2==5):
                print("Sólo el líder puede estar en la posicion central.")
                reiniciar = 1     
            if((tablero[final][final2]%100)/10 == turnos + 0.1 and tablero[final][final2] != tablero[inicio][inicio2]   ):
                print("No se pueden capturar piezas de tu mismo equipo.")
                reiniciar = 1
            if(tablero[inicio][inicio2]/100==1.11 and (final-inicio<-2 or final-inicio>2 or final2-inicio2<-2 or final2-inicio2>2)):
               print("Los militantes sólo pueden moverse una o dos casillas.")
               reiniciar =1
               #movimientos
            if(inicio2==final2):
               vertical=1
               print("", end ="")
            elif(inicio==final):
               horizontal=1
               print("", end ="")   
            elif((inicio+1==final and inicio2+1==final2) or (inicio+2==final and inicio2+2==final2) or (inicio+3==final and inicio2+3==final2) or (inicio+4==final and inicio2+4==final2) or (inicio+5==final and inicio2+5==final2) or (inicio+6==final and inicio2+6==final2) or (inicio+7==final and inicio2+7==final2) or (inicio+8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=1
            elif((inicio-1==final and inicio2-1==final2) or (inicio-2==final and inicio2-2==final2) or (inicio-3==final and inicio2-3==final2) or (inicio-4==final and inicio2-4==final2) or (inicio-5==final and inicio2-5==final2) or (inicio-6==final and inicio2-6==final2) or (inicio-7==final and inicio2-7==final2) or (inicio-8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=2
            elif((inicio-1==final and inicio2+1==final2) or (inicio-2==final and inicio2+2==final2) or (inicio-3==final and inicio2+3==final2) or (inicio-4==final and inicio2+4==final2) or (inicio-5==final and inicio2+5==final2) or (inicio-6==final and inicio2+6==final2) or (inicio-7==final and inicio2+7==final2) or (inicio-8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=3
            elif((inicio+1==final and inicio2-1==final2) or (inicio+2==final and inicio2-2==final2) or (inicio+3==final and inicio2-3==final2) or (inicio+4==final and inicio2-4==final2) or (inicio+5==final and inicio2-5==final2) or (inicio+6==final and inicio2-6==final2) or (inicio+7==final and inicio2-7==final2) or (inicio+8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=4
            else:   
               print("Las piezas solo se pueden mover de manera vertical, horizontal o diagonal.")
               
               reiniciar=1
            com=int(tablero[inicio][inicio2]/100)    
            if(tablero[final][final2]!=0 and tablero[final][final2]%10==0 and com!=2):
               print("No puedes capturar piezas capturadas.")
               reiniciar=1
            if(tablero[final][final2]%10==1 and com==2):
               print("No puedes situarte sobre otras piezas vivas con el necromóvil.")
               reiniciar=1  
            if(com==3 and tablero[final][final2]!=0):
               print("No puedes capturar piezas directamente encima de ellas con el reportero.")
               reiniciar=1   
            if(horizontal==1):
               if(final2-inicio2>0):
                  for k in range(inicio2,final2-1,1):
                     if(tablero[inicio][k+1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        horizontal=0
               if(final2-inicio2<0):        
                  for k in range(inicio2,final2+1,-1):
                     if(tablero[inicio][k-1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        horizontal=0
                     
            if(vertical==1):
               if(final-inicio>0):
                  for k in range(inicio,final-1,1):
                     if(tablero[k+1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        vertical=0
               if(final-inicio<0):
                  for k in range(inicio,final+1,-1):
                     if(tablero[k-1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        vertical=0
            if(diagonal==1):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio+k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break            
            if(diagonal==2):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio-k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break            
            if(diagonal==3):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio-k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break
                        
            if(diagonal==4):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio+k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break                  
#empezar a capturar xdxd  o movimiento xdxd
        capturarrey= tablero[final][final2]         
        pieza=int(tablero[inicio][inicio2]/100)          
        #cuando solo mueves         
        if(tablero[final][final2] == 0):         
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
        
        #capturar con necromovil
        if(pieza==2 and tablero[inicio][inicio2] != 0 ):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]
              tablero[final][final2] = tablero[inicio][inicio2]
              tablero[inicio][inicio2] = 0
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro.")     
           if(temporal%10==0):      
              tablero[filam][columnam] = temporal
        #capturar con provocador o diplomatico
        if(pieza==4 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]
              tablero[final][final2] = tablero[inicio][inicio2]
              tablero[inicio][inicio2] = 0
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5 and int((temporal%100)/10)!= 5)):
                 print("Las piezas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro si son un líder.")
                 reiniciar=0
                 
           if(temporal%10==1):      
              tablero[filam][columnam] = temporal
             
        #capturar con líder
        if(pieza==5 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]-1
              tablero[final][final2] = tablero[inicio][inicio2]
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (fila)   ."))
                        break
                     except ValueError:
                        print("Debes ingresar un numero entero entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
                 
           tablero[inicio][inicio2]=0      
           tablero[filam][columnam] = temporal
           



              
           #capturar con militante
        if(pieza==1 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]-1
              tablero[final][final2] = tablero[inicio][inicio2]
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
           tablero[inicio][inicio2]=0 
           tablero[filam][columnam] = temporal
         #capturar con reportero
        if(pieza==3):
           actualizar()
           reiniciar==0
           while True:
              while True:
                 try:
                    cr= int(input("\033[1;37;40m¿Desea capturar alguna pieza con el reportero? (1.-si 0.-no )   ."))
                    break
                 except ValueError:
                     print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
              if(cr==0 or cr==1):
                  break
              print("Debe ingresar 1 ó 0.")
           if(cr==1):
               while (reiniciar==0):
                 reiniciar=1 
                 while True:
                    while True:
                       try:
                          filam = int(input("\033[1;37;40m ¿Qué pieza desea capturar? (fila)   ."))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                    if(filam<10 and filam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 while True:
                    while True:
                       try:
                          columnam = int(input("\033[1;37;40m¿Qué pieza desea capturar? (columna)  ."))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                    if(columnam<10 and columnam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 if((final+1==filam and final2==columnam) or (final-1==filam and final2==columnam) or (final==filam and final2==columnam+1) or (final==filam and final2==columnam-1)):
                     print("", end="")
                 else:
                     print("El reportero solo puede capturar piezas adyacentes horizontales o verticales.")
                     reiniciar=0
                 if(tablero[filam][columnam]==0):
                    print("No hay pieza ahí para capturar.")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
               tablero[inicio][inicio2]=0 
               tablero[filam][columnam] = tablero[filam][columnam]-1
              
        #capturar con asesino
        if(pieza==6 and tablero[inicio][inicio2] != 0):
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = temporal

         #darte las piezas de otro equipo si te comes un rey
        eq=int((capturarrey%100)/10)
        suma=(((turnos*10)+1))-((eq*10)+1)
        if(int(capturarrey/100)==5):
           cs=0
           for x in range (0,10):
              for y in range (0,10):
                 cs=cs+1 
                 pieza=int(tablero[x][y]/100)   
                 color=int((tablero[x][y]%100)/10)
                 status=int(tablero[x][y]%10)
                 if(pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==2 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==3 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==4 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(pieza==2 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==3 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==4 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==5 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==6 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                   
            
           
           
           

    if (turnos == 2 and sr2==1):
        reiniciar = 0
        
        while(reiniciar == 0):
            reiniciar = 1
            while True:
               while True:
                  try:
                     inicio = int(input("\033[1;37;40m¿Qué pieza desea mover? (fila)   ."))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
               if(inicio<10 and inicio>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     inicio2 = int(input("\033[1;37;40m¿Qué pieza desea mover? (columna)  ."))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
                     
               if(inicio2<10 and inicio2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            
            if(tablero[inicio][inicio2]== 0):
              print("No hay pieza en ese lugar.")
              reiniciar = 0
            if(tablero[inicio][inicio2]%10==10):
               print("No puedes seleccionar piezas capturadas.")
               reiniciar=0
            if((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (tablero[inicio+1][inicio2-1]==0 and inicio2-1>0 and inicio+1<10) or (tablero[inicio+1][inicio2]==0 and inicio+1<10) or (tablero[inicio+1][inicio2+1]==0 and inicio2+1<10 and inicio+1<10) or (tablero[inicio][inicio2+1]==0 and  inicio2+1<10) or (tablero[inicio-1][inicio2+1]==0 and  inicio2+1<10 and inicio-1>0)):
               print(" ",end="")
            else:   
               print("No puedes escoger una pieza encerrada.")
               reiniciar=0
              
            
            
            if(((tablero[inicio][inicio2]%100)/10 != turnos + 0.1) and tablero[inicio][inicio2]!= 0 ):
               print("Esa pieza no es de tu  equipo.")
               reiniciar = 0
            
              
               
                
        while (reiniciar==1):
            reiniciar = 0
            while True:
               while True:
                  try:
                     final = int(input("¿A dónde la quiere mover? (fila)   ."))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final<10 and final>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     final2 = int(input("¿A dónde la quiere mover? (columna)   ."))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final2<10 and final2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")

            if(tablero[final][final2] == tablero[inicio][inicio2] and tablero[final][final2] != 0 ):
                print("No se puede mover al mismo lugar.")
                reiniciar = 1
            if(int(tablero[inicio][inicio2]/100)!=5 and final==5 and final2==5):
                print("Sólo el líder puede estar en la posicion central.")
                reiniciar = 1     
            if((tablero[final][final2]%100)/10 == turnos + 0.1 and tablero[final][final2] != tablero[inicio][inicio2]   ):
                print("No se pueden piezas de tu mismo equipo.")
                reiniciar = 1
            if(tablero[inicio][inicio2]/100==1.11 and (final-inicio<-2 or final-inicio>2 or final2-inicio2<-2 or final2-inicio2>2)):
               print("Los militantes sólo pueden moverse una o dos casillas.")
               reiniciar =1
               #movimientos
            if(inicio2==final2):
               vertical=1
               print("", end ="")
            elif(inicio==final):
               horizontal=1
               print("", end ="")   
            elif((inicio+1==final and inicio2+1==final2) or (inicio+2==final and inicio2+2==final2) or (inicio+3==final and inicio2+3==final2) or (inicio+4==final and inicio2+4==final2) or (inicio+5==final and inicio2+5==final2) or (inicio+6==final and inicio2+6==final2) or (inicio+7==final and inicio2+7==final2) or (inicio+8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=1
            elif((inicio-1==final and inicio2-1==final2) or (inicio-2==final and inicio2-2==final2) or (inicio-3==final and inicio2-3==final2) or (inicio-4==final and inicio2-4==final2) or (inicio-5==final and inicio2-5==final2) or (inicio-6==final and inicio2-6==final2) or (inicio-7==final and inicio2-7==final2) or (inicio-8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=2
            elif((inicio-1==final and inicio2+1==final2) or (inicio-2==final and inicio2+2==final2) or (inicio-3==final and inicio2+3==final2) or (inicio-4==final and inicio2+4==final2) or (inicio-5==final and inicio2+5==final2) or (inicio-6==final and inicio2+6==final2) or (inicio-7==final and inicio2+7==final2) or (inicio-8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=3
            elif((inicio+1==final and inicio2-1==final2) or (inicio+2==final and inicio2-2==final2) or (inicio+3==final and inicio2-3==final2) or (inicio+4==final and inicio2-4==final2) or (inicio+5==final and inicio2-5==final2) or (inicio+6==final and inicio2-6==final2) or (inicio+7==final and inicio2-7==final2) or (inicio+8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=4
            else:   
               print("Las piezas solo se pueden mover de manera vertical, horizontal o diagonal.")
               
               reiniciar=1
            com=int(tablero[inicio][inicio2]/100)    
            if(tablero[final][final2]!=0 and tablero[final][final2]%10==0 and com!=2):
               print("No puedes capturar piezas capturadas.")
               reiniciar=1
            if(tablero[final][final2]%10==1 and com==2):
               print("No puedes situarte sobre otras piezas vivas con el necromóvil.")
               reiniciar=1  
            if(com==3 and tablero[final][final2]!=0):
               print("No puedes capturar piezas directamente encima de ellas con el reportero.")
               reiniciar=1   
            if(horizontal==1):
               if(final2-inicio2>0):
                  for k in range(inicio2,final2-1,1):
                     if(tablero[inicio][k+1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        horizontal=0
               if(final2-inicio2<0):        
                  for k in range(inicio2,final2+1,-1):
                     if(tablero[inicio][k-1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        horizontal=0
                     
            if(vertical==1):
               if(final-inicio>0):
                  for k in range(inicio,final-1,1):
                     if(tablero[k+1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        vertical=0
               if(final-inicio<0):
                  for k in range(inicio,final+1,-1):
                     if(tablero[k-1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        vertical=0
            if(diagonal==1):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio+k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break            
            if(diagonal==2):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio-k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break            
            if(diagonal==3):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio-k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break
                        
            if(diagonal==4):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio+k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break
                     
                           

               
            
                  
#empezar a capturar xdxd  o movimiento xdxd
        capturarrey= tablero[final][final2]         
        pieza=int(tablero[inicio][inicio2]/100)          
        #cuando solo mueves         
        if(tablero[final][final2] == 0):         
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
        
        #capturar con necromovil
        if(pieza==2 and tablero[inicio][inicio2] != 0 ):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]
              tablero[final][final2] = tablero[inicio][inicio2]
              tablero[inicio][inicio2] = 0
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro.")     
           if(temporal%10==0):      
              tablero[filam][columnam] = temporal
        #capturar con provocador o diplomatico
        if(pieza==4 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]
              tablero[final][final2] = tablero[inicio][inicio2]
              tablero[inicio][inicio2] = 0
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5 and int((temporal%100)/10)!= 5)):
                 print("Las piezas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro si son un líder.")
                 reiniciar=0
                 
           if(temporal%10==1):      
              tablero[filam][columnam] = temporal
             
        #capturar con líder
        if(pieza==5 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]-1
              tablero[final][final2] = tablero[inicio][inicio2]
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (fila)   ."))
                        break
                     except ValueError:
                        print("Debes ingresar un numero entero entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
                 
           tablero[inicio][inicio2]=0      
           tablero[filam][columnam] = temporal
           



              
           #capturar con militante
        if(pieza==1 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]-1
              tablero[final][final2] = tablero[inicio][inicio2]
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
           tablero[inicio][inicio2]=0 
           tablero[filam][columnam] = temporal
         #capturar con reportero
        if(pieza==3):
           actualizar()
           reiniciar==0
           while True:
              while True:
                 try:
                    cr= int(input("\033[1;37;40mdesea capturar alguna pieza con el reportero? (1.-si 0.-no )   ."))
                    break
                 except ValueError:
                     print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
              if(cr==0 or cr==1):
                  break
              print("Debe ingresar 1 o 0.")
           if(cr==1):
               while (reiniciar==0):
                 reiniciar=1 
                 while True:
                    while True:
                       try:
                          filam = int(input("\033[1;37;40m¿Qué pieza desea capturar? (fila)   ."))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                    if(filam<10 and filam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 while True:
                    while True:
                       try:
                          columnam = int(input("\033[1;37;40m¿Qué pieza desea capturar? (columna)  ."))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                    if(columnam<10 and columnam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 if((final+1==filam and final2==columnam) or (final-1==filam and final2==columnam) or (final==filam and final2==columnam+1) or (final==filam and final2==columnam-1)):
                     print("", end="")
                 else:
                     print("El reportero solo puede capturar piezas adyacentes horizontales o verticales.")
                     reiniciar=0
                 if(tablero[filam][columnam]==0):
                    print("No hay pieza ahí para capturar.")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas.")
                    reiniciar=0
               tablero[inicio][inicio2]=0 
               tablero[filam][columnam] = tablero[filam][columnam]-1
              
        #capturar con asesino
        if(pieza==6 and tablero[inicio][inicio2] != 0):
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = temporal

         #darte las piezas de otro equipo si te comes un rey
        eq=int((capturarrey%100)/10)
        suma=(((turnos*10)+1))-((eq*10)+1)
        if(int(capturarrey/100)==5):
           cs=0
           for x in range (0,10):
              for y in range (0,10):
                 cs=cs+1 
                 pieza=int(tablero[x][y]/100)   
                 color=int((tablero[x][y]%100)/10)
                 status=int(tablero[x][y]%10)
                 if(pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==2 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==3 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==4 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(pieza==2 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==3 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==4 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==5 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==6 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                   
                     
        
    if (turnos == 3 and sr3==1):
        reiniciar = 0
        
        while(reiniciar == 0):
            reiniciar = 1
            while True:
               while True:
                  try:
                     inicio = int(input("\033[1;37;40m¿Qué pieza desea mover? (fila)   ."))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
               if(inicio<10 and inicio>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     inicio2 = int(input("\033[1;37;40m¿Qué pieza desea mover? (columna)  ."))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
                     
               if(inicio2<10 and inicio2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            
            if(tablero[inicio][inicio2]== 0):
              print("No hay pieza en ese lugar.")
              reiniciar = 0
            if(tablero[inicio][inicio2]%10==10):
               print("No puedes seleccionar piezas capturadas.")
               reiniciar=0
            if((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (tablero[inicio+1][inicio2-1]==0 and inicio2-1>0 and inicio+1<10) or (tablero[inicio+1][inicio2]==0 and inicio+1<10) or (tablero[inicio+1][inicio2+1]==0 and inicio2+1<10 and inicio+1<10) or (tablero[inicio][inicio2+1]==0 and  inicio2+1<10) or (tablero[inicio-1][inicio2+1]==0 and  inicio2+1<10 and inicio-1>0)):
               print(" ",end="")
            else:   
               print("No puedes escoger una pieza encerrada.")
               reiniciar=0
              
            
            
            if(((tablero[inicio][inicio2]%100)/10 != turnos + 0.1) and tablero[inicio][inicio2]!= 0 ):
               print("Esa pieza no es de tu  equipo.")
               reiniciar = 0
            
              
               
                
        while (reiniciar==1):
            reiniciar = 0
            while True:
               while True:
                  try:
                     final = int(input("¿A dónde la quiere mover? (fila)   ."))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final<10 and final>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     final2 = int(input("¿A dónde la quiere mover? (columna)   ."))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final2<10 and final2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")

            if(tablero[final][final2] == tablero[inicio][inicio2] and tablero[final][final2] != 0 ):
                print("No se puede mover al mismo lugar.")
                reiniciar = 1
            if(int(tablero[inicio][inicio2]/100)!=5 and final==5 and final2==5):
                print("Sólo el líder puede estar en la posicion central.")
                reiniciar = 1     
            if((tablero[final][final2]%100)/10 == turnos + 0.1 and tablero[final][final2] != tablero[inicio][inicio2]   ):
                print("No se pueden piezas de tu mismo equipo.")
                reiniciar = 1
            if(tablero[inicio][inicio2]/100==1.11 and (final-inicio<-2 or final-inicio>2 or final2-inicio2<-2 or final2-inicio2>2)):
               print("Los militantes sólo pueden moverse una o dos casillas.")
               reiniciar =1
               #movimientos
            if(inicio2==final2):
               vertical=1
               print("", end ="")
            elif(inicio==final):
               horizontal=1
               print("", end ="")   
            elif((inicio+1==final and inicio2+1==final2) or (inicio+2==final and inicio2+2==final2) or (inicio+3==final and inicio2+3==final2) or (inicio+4==final and inicio2+4==final2) or (inicio+5==final and inicio2+5==final2) or (inicio+6==final and inicio2+6==final2) or (inicio+7==final and inicio2+7==final2) or (inicio+8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=1
            elif((inicio-1==final and inicio2-1==final2) or (inicio-2==final and inicio2-2==final2) or (inicio-3==final and inicio2-3==final2) or (inicio-4==final and inicio2-4==final2) or (inicio-5==final and inicio2-5==final2) or (inicio-6==final and inicio2-6==final2) or (inicio-7==final and inicio2-7==final2) or (inicio-8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=2
            elif((inicio-1==final and inicio2+1==final2) or (inicio-2==final and inicio2+2==final2) or (inicio-3==final and inicio2+3==final2) or (inicio-4==final and inicio2+4==final2) or (inicio-5==final and inicio2+5==final2) or (inicio-6==final and inicio2+6==final2) or (inicio-7==final and inicio2+7==final2) or (inicio-8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=3
            elif((inicio+1==final and inicio2-1==final2) or (inicio+2==final and inicio2-2==final2) or (inicio+3==final and inicio2-3==final2) or (inicio+4==final and inicio2-4==final2) or (inicio+5==final and inicio2-5==final2) or (inicio+6==final and inicio2-6==final2) or (inicio+7==final and inicio2-7==final2) or (inicio+8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=4
            else:   
               print("Las piezas solo se pueden mover de manera vertical, horizontal o diagonal.")
               
               reiniciar=1
            com=int(tablero[inicio][inicio2]/100)    
            if(tablero[final][final2]!=0 and tablero[final][final2]%10==0 and com!=2):
               print("No puedes capturar piezas capturadas.")
               reiniciar=1
            if(tablero[final][final2]%10==1 and com==2):
               print("No puedes situarte sobre otras piezas vivas con el necromóvil.")
               reiniciar=1  
            if(com==3 and tablero[final][final2]!=0):
               print("No puedes capturar piezas directamente encima de ellas con el reportero.")
               reiniciar=1   
            if(horizontal==1):
               if(final2-inicio2>0):
                  for k in range(inicio2,final2-1,1):
                     if(tablero[inicio][k+1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        horizontal=0
               if(final2-inicio2<0):        
                  for k in range(inicio2,final2+1,-1):
                     if(tablero[inicio][k-1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        horizontal=0
                     
            if(vertical==1):
               if(final-inicio>0):
                  for k in range(inicio,final-1,1):
                     if(tablero[k+1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        vertical=0
               if(final-inicio<0):
                  for k in range(inicio,final+1,-1):
                     if(tablero[k-1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        vertical=0
            if(diagonal==1):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio+k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break            
            if(diagonal==2):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio-k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break            
            if(diagonal==3):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio-k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break
                        
            if(diagonal==4):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio+k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break
                     
                           

               
            
                  
#empezar a capturar xdxd  o movimiento xdxd
        capturarrey= tablero[final][final2]         
        pieza=int(tablero[inicio][inicio2]/100)          
        #cuando solo mueves         
        if(tablero[final][final2] == 0):         
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
        
        #capturar con necromovil
        if(pieza==2 and tablero[inicio][inicio2] != 0 ):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]
              tablero[final][final2] = tablero[inicio][inicio2]
              tablero[inicio][inicio2] = 0
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro.")     
           if(temporal%10==0):      
              tablero[filam][columnam] = temporal
        #capturar con provocador o diplomatico
        if(pieza==4 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]
              tablero[final][final2] = tablero[inicio][inicio2]
              tablero[inicio][inicio2] = 0
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5 and int((temporal%100)/10)!= 5)):
                 print("Las piezas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro si son un líder.")
                 reiniciar=0
                 
           if(temporal%10==1):      
              tablero[filam][columnam] = temporal
             
        #capturar con líder
        if(pieza==5 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]-1
              tablero[final][final2] = tablero[inicio][inicio2]
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (fila)   ."))
                        break
                     except ValueError:
                        print("Debes ingresar un numero entero entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
                 
           tablero[inicio][inicio2]=0      
           tablero[filam][columnam] = temporal
           



              
           #capturar con militante
        if(pieza==1 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]-1
              tablero[final][final2] = tablero[inicio][inicio2]
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
           tablero[inicio][inicio2]=0 
           tablero[filam][columnam] = temporal
         #capturar con reportero
        if(pieza==3):
           actualizar()
           reiniciar==0
           while True:
              while True:
                 try:
                    cr= int(input("\033[1;37;40mdesea capturar alguna pieza con el reportero? (1.-si 0.-no )   ."))
                    break
                 except ValueError:
                     print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
              if(cr==0 or cr==1):
                  break
              print("Debe ingresar 1 ó 0.")
           if(cr==1):
               while (reiniciar==0):
                 reiniciar=1 
                 while True:
                    while True:
                       try:
                          filam = int(input("\033[1;37;40m¿Qué pieza desea capturar? (fila)   ."))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                    if(filam<10 and filam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 while True:
                    while True:
                       try:
                          columnam = int(input("\033[1;37;40m¿Qué pieza desea capturar? (columna)  ."))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                    if(columnam<10 and columnam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 if((final+1==filam and final2==columnam) or (final-1==filam and final2==columnam) or (final==filam and final2==columnam+1) or (final==filam and final2==columnam-1)):
                     print("", end="")
                 else:
                     print("El reportero sólo puede capturar piezas adyacentes horizontales o verticales.")
                     reiniciar=0
                 if(tablero[filam][columnam]==0):
                    print("No hay pieza ahí para capturar.")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas.")
                    reiniciar=0
               tablero[inicio][inicio2]=0 
               tablero[filam][columnam] = tablero[filam][columnam]-1
              
        #capturar con asesino
        if(pieza==6 and tablero[inicio][inicio2] != 0):
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = temporal

         #darte las piezas de otro equipo si te comes un rey
        eq=int((capturarrey%100)/10)
        suma=(((turnos*10)+1))-((eq*10)+1)
        if(int(capturarrey/100)==5):
           cs=0
           for x in range (0,10):
              for y in range (0,10):
                 cs=cs+1 
                 pieza=int(tablero[x][y]/100)   
                 color=int((tablero[x][y]%100)/10)
                 status=int(tablero[x][y]%10)
                 if(pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==2 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==3 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==4 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(pieza==2 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==3 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==4 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==5 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==6 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                   
        
        
    if(turnos == 4 and sr4==1):
        reiniciar = 0
        while(reiniciar == 0):
            reiniciar = 1
            while True:
               while True:
                  try:
                     inicio = int(input("\033[1;37;40m¿Qué pieza desea mover? (fila)   ."))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
               if(inicio<10 and inicio>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     inicio2 = int(input("\033[1;37;40m¿Qué pieza desea mover? (columna)  ."))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
                     
               if(inicio2<10 and inicio2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            
            if(tablero[inicio][inicio2]== 0):
              print("No hay pieza en ese lugar.")
              reiniciar = 0
            if(tablero[inicio][inicio2]%10==10):
               print("No puedes seleccionar piezas capturadas.")
               reiniciar=0
            if((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (tablero[inicio+1][inicio2-1]==0 and inicio2-1>0 and inicio+1<10) or (tablero[inicio+1][inicio2]==0 and inicio+1<10) or (tablero[inicio+1][inicio2+1]==0 and inicio2+1<10 and inicio+1<10) or (tablero[inicio][inicio2+1]==0 and  inicio2+1<10) or (tablero[inicio-1][inicio2+1]==0 and  inicio2+1<10 and inicio-1>0)):
               print(" ",end="")
            else:   
               print("No puedes escoger una pieza encerrada.")
               reiniciar=0
              
            
            
            if(((tablero[inicio][inicio2]%100)/10 != turnos + 0.1) and tablero[inicio][inicio2]!= 0 ):
               print("Esa pieza no es de tu  equipo.")
               reiniciar = 0
            
              
               
                
        while (reiniciar==1):
            reiniciar = 0
            while True:
               while True:
                  try:
                     final = int(input("¿A dónde la quiere mover? (fila)   ."))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final<10 and final>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     final2 = int(input("¿A dónde la quiere mover? (columna)   ."))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final2<10 and final2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")

            if(tablero[final][final2] == tablero[inicio][inicio2] and tablero[final][final2] != 0 ):
                print("No se puede mover al mismo lugar.")
                reiniciar = 1
            if(int(tablero[inicio][inicio2]/100)!=5 and final==5 and final2==5):
                print("Sólo el líder puede estar en la posicion central.")
                reiniciar = 1     
            if((tablero[final][final2]%100)/10 == turnos + 0.1 and tablero[final][final2] != tablero[inicio][inicio2]   ):
                print("No se pueden piezas de tu mismo equipo.")
                reiniciar = 1
            if(tablero[inicio][inicio2]/100==1.11 and (final-inicio<-2 or final-inicio>2 or final2-inicio2<-2 or final2-inicio2>2)):
               print("Los militantes sólo pueden moverse una o dos casillas.")
               reiniciar =1
               #movimientos
            if(inicio2==final2):
               vertical=1
               print("", end ="")
            elif(inicio==final):
               horizontal=1
               print("", end ="")   
            elif((inicio+1==final and inicio2+1==final2) or (inicio+2==final and inicio2+2==final2) or (inicio+3==final and inicio2+3==final2) or (inicio+4==final and inicio2+4==final2) or (inicio+5==final and inicio2+5==final2) or (inicio+6==final and inicio2+6==final2) or (inicio+7==final and inicio2+7==final2) or (inicio+8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=1
            elif((inicio-1==final and inicio2-1==final2) or (inicio-2==final and inicio2-2==final2) or (inicio-3==final and inicio2-3==final2) or (inicio-4==final and inicio2-4==final2) or (inicio-5==final and inicio2-5==final2) or (inicio-6==final and inicio2-6==final2) or (inicio-7==final and inicio2-7==final2) or (inicio-8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=2
            elif((inicio-1==final and inicio2+1==final2) or (inicio-2==final and inicio2+2==final2) or (inicio-3==final and inicio2+3==final2) or (inicio-4==final and inicio2+4==final2) or (inicio-5==final and inicio2+5==final2) or (inicio-6==final and inicio2+6==final2) or (inicio-7==final and inicio2+7==final2) or (inicio-8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=3
            elif((inicio+1==final and inicio2-1==final2) or (inicio+2==final and inicio2-2==final2) or (inicio+3==final and inicio2-3==final2) or (inicio+4==final and inicio2-4==final2) or (inicio+5==final and inicio2-5==final2) or (inicio+6==final and inicio2-6==final2) or (inicio+7==final and inicio2-7==final2) or (inicio+8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=4
            else:   
               print("Las piezas solo se pueden mover de manera vertical, horizontal o diagonal.")
               
               reiniciar=1
            com=int(tablero[inicio][inicio2]/100)    
            if(tablero[final][final2]!=0 and tablero[final][final2]%10==0 and com!=2):
               print("No puedes capturar piezas capturadas.")
               reiniciar=1
            if(tablero[final][final2]%10==1 and com==2):
               print("No puedes situarte sobre otras piezas vivas con el necromóvil.")
               reiniciar=1  
            if(com==3 and tablero[final][final2]!=0):
               print("No puedes capturar piezas directamente encima de ellas con el reportero.")
               reiniciar=1   
            if(horizontal==1):
               if(final2-inicio2>0):
                  for k in range(inicio2,final2-1,1):
                     if(tablero[inicio][k+1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        horizontal=0
               if(final2-inicio2<0):        
                  for k in range(inicio2,final2+1,-1):
                     if(tablero[inicio][k-1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        horizontal=0
                     
            if(vertical==1):
               if(final-inicio>0):
                  for k in range(inicio,final-1,1):
                     if(tablero[k+1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        vertical=0
               if(final-inicio<0):
                  for k in range(inicio,final+1,-1):
                     if(tablero[k-1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
                        vertical=0
            if(diagonal==1):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio+k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break            
            if(diagonal==2):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio-k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break            
            if(diagonal==3):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio-k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break
                        
            if(diagonal==4):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio+k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     diagonal=0
                     break
                     
                           

               
            
                  
#empezar a capturar xdxd  o movimiento xdxd
        capturarrey= tablero[final][final2]         
        pieza=int(tablero[inicio][inicio2]/100)          
        #cuando solo mueves         
        if(tablero[final][final2] == 0):         
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
        
        #capturar con necromovil
        if(pieza==2 and tablero[inicio][inicio2] != 0 ):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]
              tablero[final][final2] = tablero[inicio][inicio2]
              tablero[inicio][inicio2] = 0
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro.")     
           if(temporal%10==0):      
              tablero[filam][columnam] = temporal
        #capturar con provocador o diplomatico
        if(pieza==4 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]
              tablero[final][final2] = tablero[inicio][inicio2]
              tablero[inicio][inicio2] = 0
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza sobre la que está? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5 and int((temporal%100)/10)!= 5)):
                 print("Las piezas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro si son un líder.")
                 reiniciar=0
                 
           if(temporal%10==1):      
              tablero[filam][columnam] = temporal
             
        #capturar con líder
        if(pieza==5 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]-1
              tablero[final][final2] = tablero[inicio][inicio2]
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (fila)   ."))
                        break
                     except ValueError:
                        print("Debes ingresar un numero entero entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
                 
           tablero[inicio][inicio2]=0      
           tablero[filam][columnam] = temporal
           



              
           #capturar con militante
        if(pieza==1 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           while (reiniciar==0):
              reiniciar = 1
              temporal=tablero[final][final2]-1
              tablero[final][final2] = tablero[inicio][inicio2]
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (fila)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40ma ¿Dónde desea mover la pieza capturada? (columna)   ."))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
           tablero[inicio][inicio2]=0 
           tablero[filam][columnam] = temporal
         #capturar con reportero
        if(pieza==3):
           actualizar()
           reiniciar==0
           while True:
              while True:
                 try:
                    cr= int(input("\033[1;37;40m¿Desea capturar alguna pieza con el reportero? (1.-si 0.-no )   ."))
                    break
                 except ValueError:
                     print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
              if(cr==0 or cr==1):
                  break
              print("Debe ingresar 1 ó 0.")
           if(cr==1):
               while (reiniciar==0):
                 reiniciar=1 
                 while True:
                    while True:
                       try:
                          filam = int(input("\033[1;37;40m¿Qué pieza desea capturar? (fila)   ."))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                    if(filam<10 and filam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 while True:
                    while True:
                       try:
                          columnam = int(input("\033[1;37;40m¿Qué pieza desea capturar? (columna)  ."))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar numeros enteros entre 1 y 9.")
                    if(columnam<10 and columnam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 if((final+1==filam and final2==columnam) or (final-1==filam and final2==columnam) or (final==filam and final2==columnam+1) or (final==filam and final2==columnam-1)):
                     print("", end="")
                 else:
                     print("El reportero solo puede capturar piezas adyacentes horizontales o verticales.")
                     reiniciar=0
                 if(tablero[filam][columnam]==0):
                    print("No hay pieza ahí para capturar.")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas.")
                    reiniciar=0
               tablero[inicio][inicio2]=0 
               tablero[filam][columnam] = tablero[filam][columnam]-1
              
        #capturar con asesino
        if(pieza==6 and tablero[inicio][inicio2] != 0):
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = temporal

         #darte las piezas de otro equipo si te comes un rey
        eq=int((capturarrey%100)/10)
        suma=(((turnos*10)+1))-((eq*10)+1)
        if(int(capturarrey/100)==5):
           cs=0
           for x in range (0,10):
              for y in range (0,10):
                 cs=cs+1 
                 pieza=int(tablero[x][y]/100)   
                 color=int((tablero[x][y]%100)/10)
                 status=int(tablero[x][y]%10)
                 if(pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==2 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==3 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==4 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(pieza==2 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==3 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==4 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==5 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==6 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                   
        

                
    if(tablero[5][5]!=0):
       poder=1
    elif(tablero[5][5]==0):
       poder=0
       
    if(poder==0):    
       if(turnos==4):
          turnos = 0
       turnos = turnos + contadorturnos
       contadorpoder=contadorturnos+1
       if(contadorturnos==4):
          contadorturnos=1
       
    if(poder==1):
       if(contadorpoder==0):
          turnos=turnos+contadorturnos
          contadorturnos=contadorturnos+1
          
          if(contadorturnos==4):
             contadorturnos=1
       if(contadorpoder==1):
          turnos=int((tablero[5][5]%100)/10)
          contadorpoder=-1
       contadorpoder=contadorpoder+1   
    #checar que solo haya un rey vivo
    for x in range (0,10):
       for y in range (0,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          if(color==1 and pieza==5):
             rey1=tablero[x][y]
             s1=status
          if(color==2 and pieza==5):
             rey2=tablero[x][y]
             s2=status
          if(color==3 and pieza==5):
             rey3=tablero[x][y]
             s3=status
          if(color==4 and pieza==5):
             rey4=tablero[x][y]
             s4=status
    if(s1+s2+s3+s4==1):
       terminar=1
clear()
print("Game over.")
if(s1==1):
   print("Ha ganado el jugador 1 (azul).")
if(s2==1):
   print("Ha ganado el jugador 2 (rojo).")
if(s3==1):
   print("Ha ganado el jugador 3 (amarillo).")
if(s4==1):
   print("Ha ganado el jugador 4 (verde).")   
input("Pulse en enter para salir...")        
    




   



    
