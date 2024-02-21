#Pregunta 1:
#El for es un equivalente al foreach en otros lenguajes que recorre arreglos
#f{} da formato a la cadena de texto a imprimir permitiendoinos embeber una variable
#f es de format y entre las llaves podemos incorporar variables

#Pregunta2:
#recorre un arreglo de cualidades para preguntarte si una persona cumple con esas características, dependiendo de las características que si cumple te da un score
#el swich no existe pero tiene dos equivalentes, elif anidado y match case

#pregunta3:
#en la línea número 3
#hacemos el llamado directo de la función para no hacer más declaraciones de variables que solo se ocuparían una o dos veces en todo el código

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

## comandos de git para agregar el archivo

# 1 git add entregable_profe.py
# 2 git commit -m "entregable"
# 3 git push origin main