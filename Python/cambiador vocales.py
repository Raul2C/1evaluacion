def pig_latin():
    texto = raw_input("Escribe un texto")
    for cont in range(0, len(texto),1):
        if texto[cont]=="a" or texto[cont]=="A" or texto[cont]=="e" or texto[cont]=="E" or texto[cont]=="i" or texto[cont]=="I" or texto[cont]=="o" or texto[cont]=="O" or texto[cont]=="u" or texto[cont]=="U":
           print "u",
        else:
            print texto[cont],
pig_latin()
            
