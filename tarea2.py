import random
number = 0
num=random.randrange(1, 100)
while number != num:
    number = int (input ("Introduce el número : "))
    if number==num:
        print("Felicidaes es el número correcto.")
    else :
        print("Número incorrecto intenta de nuevo.")