print("Programa para convertir temperaturas en Celsius, Fahrenheit, Kelvin y Rankine \n")
escala_inicial = input("Ingresar el nombre completo de la escala de la temperatura inicial empezando con letra mayuscula \n")
if escala_inicial == "Celsius":
    temp_inicial= float(input("Ingresar en grados la temperatura inicial \n"))
    if temp_inicial > -274:
        escala_final = input("Ingresar el nombre completo de la escala a convertir empezando con letra mayuscula \n")
        if escala_final == "Fahrenheit":
            temp_final= (temp_inicial *1.8) +32
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        elif escala_final == "Kelvin":
            temp_final = (temp_inicial + 273.15)
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        elif escala_final == "Rankine":
            temp_final= (temp_inicial + 273.15) * 1.8
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        else:
            print ("Ingresar una escala valida")
    else:
        print ("Ingresar una temperatura valida")
elif escala_inicial == "Fahrenheit":
    temp_inicial= float(input("Ingresar en grados la temperatura inicial"))
    if temp_inicial > -459.67:
        escala_final = input("Ingresar el nombre completo de la escala a convertir empezando con letra mayuscula")
        if escala_final == "Celsius":
            temp_final= (temp_inicial - 32) * 0.555
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        elif escala_final == "Kelvin":
            temp_final= (temp_inicial +459.67) *0.555
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        elif escala_final == "Rankine":
            temp_final = (temp_inicial + 459.67)
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        else:
            print ("Ingresar una escala valida")
    else:
        print ("Ingresar una temperatura valida")
elif escala_inicial == "Kelvin":
    temp_inicial= float(input("Ingresar en grados la temperatura inicial"))
    if temp_inicial > -1:
        escala_final = input("Ingresar el nombre completo de la escala a convertir empezando con letra mayuscula")
        if escala_final == "Celsius":
            temp_final= (temp_inicial - 273.15)
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        elif escala_final == "Fahrenheit":
            temp_final= (temp_inicial * 1.8) - 459.67
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        elif escala_final == "Rankine":
            temp_final= temp_inicial * 1.8
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        else:
            print("Ingresar una escala valida")
    else:
            print ("Ingresar una temperatura valida")
elif escala_inicial == "Rankine":
    temp_inicial= float(input("Ingresar en grados la temperatura inicial"))
    if temp_inicial > -1:
        escala_final = input("Ingresar el nombre completo de la escala a convertir empezando con letra mayuscula")
        if escala_final == "Celsius":
            temp_final = (temp_inicial - 491.67) / 1.8
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        elif escala_final == "Fahrenheit":
            temp_final = (temp_inicial - 459.67)
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        elif escala_final == "Kelvin":
            temp_final= (temp_inicial / 1.8)
            print ("La temperatura en " + escala_final + " es " + repr(temp_final))
        else:
            print ("Ingresar una escala valida")
    else:   
        print ("Ingresar una temperatura valida")
else:
    print ("Ingresar una escala valida")
k=input("Presionar enter para salir") 