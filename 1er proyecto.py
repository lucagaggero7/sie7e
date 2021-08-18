#Calcular cuantos años faltan para que puedas conducir
edad_necesaria_para_conducir = 18
tu_nombre = (input ("COMO TE LLAMAS NENE?"))
tu_edad = int (input ("CUANTOS AÑOS TENES?"))

if tu_edad >= edad_necesaria_para_conducir:
    print ("FELICITACIONES", (tu_nombre), "ERES APTO PARA CONDUCIR")

else:
    print("LO SIENTO", (tu_nombre) ,"AUN TE FALTAN",(edad_necesaria_para_conducir - tu_edad),"AÑO/S PARA CONDUCIR")

input("Presione enter para continuar... :D")