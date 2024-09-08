import random 
mayus = int (input ("Introduce el número de mayúsculas que desea que tenga la contraseña: "))
minus = int (input ("Introduce el número de minúsculas que desea que tenga la contraseña: "))
digit = int (input ("Introduce el número de dígitos que desea que tenga la contraseña: "))
i=0
caster=0
cadena="" 
while i<mayus:
    caster=random.randrange(65, 90, 1)
    cadena=cadena + chr(caster)
    i+=1
i=0
while i<minus:
    caster=random.randrange(97, 122, 1)
    cadena=cadena + chr(caster)
    i+=1
i=0
while i<digit:
    caster=random.randrange(0, 9, 1)
    cadena=cadena + str(caster)
    i+=1
lista=list(cadena)
random.shuffle(lista)
for j in lista :
    cadena+=j
print (cadena)