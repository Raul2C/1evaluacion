def multiplicador():
    n = input("Dime que tabala quieres calcular")
    print"Tabla del",n
    for cont in range(1, 11, 1):
        print n,"x",cont,"=",n * cont
multiplicador()
