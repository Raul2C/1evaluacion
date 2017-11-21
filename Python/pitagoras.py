def pitagoras():
    lado1=input("Dime la medida del primer lado")
    lado2=input("Dime la medida del segundo lado")
    lado3=input("Dime la medida del tercer lado")
    if(lado1*lado1+lado2*lado2==lado3*lado3)or(lado2*lado2+lado3*lado3==lado1*lado1)or(lado3*lado3+lado1*lado1==lado2*lado2):
        print"El triangulo es rectangulo"
    else:
        print"El triangulo no es rectangulo"
pitagoras()
    
