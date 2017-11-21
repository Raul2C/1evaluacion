def mayor(numero,numero2):
    if (numero>numero2):
        respuesta= numero
    if(numero<numero2):
        respuesta=numero2
    else:
        respuesta="Los dos numeros son iguales"
    return respuesta

def comparadorprincipal():
    numero=input("Dime un numero")
    numero2=input("Dime otro numero y te digo cual es mayor")
    print mayor(numero,numero2)
comparadorprincipal()
