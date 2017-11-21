def giradorcifras():
    numero=input("Dime un numero")
    for cont in range(int(numero),0,1):
        while numero>1:
            cifra=numero%10
            numero=numero/10
        print cifra[cont]
giradorcifras()
    
