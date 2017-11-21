def contadorparesimpares():
    numero=input("Dime un numero")
    n_cifrasP=0
    n_cifrasI=0
    while numero>1:
        cifra = numero%10
        if cifra%2==0:
            n_cifrasP = n_cifrasP + 1
        if cifra%2==1:
            n_cifrasI=n_cifrasI + 1
        numero=numero/10
    print"Tiene", n_cifrasP,"cifras pares y", n_cifrasI,"cifras impares"
contadorparesimpares()
