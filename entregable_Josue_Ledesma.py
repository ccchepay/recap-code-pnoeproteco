#Ledesma Cortés Josué

#Respuestas del cuestionario 

"""
Pregunta 1. 
El bucle for itera sobre la secuencia hasta que se hayan procesado todos los elementos, y luego el control del programa continúa con la siguiente instrucción después del bloque for
La función "f{}" se utiliza para crear una f-string, que es una cadena de formato literal. Las f-strings proporcionan una forma más conveniente y legible de formatear cadenas. Las f-strings permiten insertar valores de variables directamente dentro de una cadena, lo que facilita la creación de cadenas con formato sin la necesidad de concatenación o funciones adicionales

Pregunta 2.
El código está diseñado para recorrer todos los valores dentro de una fila y con cada uno de esos valores pregunta si la persona en cuestión cumple con alguna de esas características
La función SWITCH no existe en python

Pregunta 3.
El arreglo que se contiene las cualidades está declarado en la línea 19
En este código la función es llamada directamente porque no se utiliza siempre, entonces la manera de utilizarla de manera más óptima es llamarla directamente cuando se va a utilizar.


"""


##arrays declaration
array = [1,2,3,4,5,6,7,8,9,10]
qualities=["alto","bronceado","guapo","rico","sexy","tierno","rudo"]

#hello world
print("hello world")

##for loop and if
for i in range(1,10):
    if(i%2!=0):
        print(f"{i} no es par")

##for loop?
 for i in array:
     if(i%2!=0):
         print(f"{i} no es par")

#python and switch and read options
 for quality in qualities:
     prompt=input(f"Es {quality}? (Y/N)")
     if(prompt=='N'):
         print("no te conviene")
         break
 if(prompt =='Y'):
     print("Apurese o se lo ganan")

##append to array
 if(input("Deseas agregar más condiciones?(Y/N)")=="Y"):
     qualities.append(input("Escribe la propiedad: "))

##print array
 print("Quealities:")
 print (qualities)

# ## While
 flag = True
 while(flag):
     if(input("Deseas agregar más condiciones?(Y/N)")=="Y"):
         qualities.append(input("Escribe la propiedad: "))
     else:
         flag=False
 print("Quealities:")
 print (qualities)

#FUNCIONES
def imprimir_cualidades(cualidades):
    print(cualidades)

def agregar_cualidades(cualidades):
    flag=True
    while(flag):
        if(input("Deseas agregar más condiciones?(Y/N)")=="Y"):
            cualidades.append(input("Escribe la propiedad: "))
        else:
            flag=False
        
def cuestionar_cualidades(cualidades):
    score=0
    for cualidad in cualidades:
        prompt=input(f"Es {cualidad}? (Y/N)")
        if(prompt!='N'):
            score=score+1
    return score

def calcular_score(score,len):
    if((score/len)==1):
            print("Es perfecto")
    elif((score/len)>=.8):
            print("Apliquese o se lo ganan")
    elif((score/len)>=.6):
            print("Momeno")
    elif((score/len)>=.4):
            print("No te lo recomiendo")
    elif((score/len)<=.2):
            print("orre y no mires atrás")
#VARIABLES
qualities=["alto","bronceado","guapo","rico","sexy","tierno","rudo"]

#programa

print("Vamos a ver si la persona que piensas te conviene")
print("Estas son las cualidades que actualmente validamos")
imprimir_cualidades(qualities)
agregar_cualidades(qualities)
print("vamos a comenzar")

score = cuestionar_cualidades(qualities)
calcular_score(score,len(qualities))

