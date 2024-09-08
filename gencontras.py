import itertools

archivo_entrada = 'personas.txt' 
archivo_salida = 'contraseñas_generadas.txt' 

def cambiar_letras_por_numeros(palabra):
    reemplazos = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 'g': '9'}
    return ''.join(reemplazos.get(c, c) for c in palabra)

def cambiar_numeros_por_letras(palabra):
    reemplazos = {'1': 'i', '3': 'e', '4': 'a', '5': 's', '0': 'o', '9': 'g'}
    return ''.join(reemplazos.get(c, c) for c in palabra)

def generar_variaciones(palabra):
    variaciones = []
    variaciones.append(palabra)
    variaciones.append(cambiar_letras_por_numeros(palabra))
    variaciones.append(cambiar_numeros_por_letras(palabra))
    
def generar_contraseñas(archivo_entrada, archivo_salida):
    contraseñas = []

    with open(archivo_entrada, 'r') as archivo:
        palabras = archivo.read().splitlines()

    for palabra in palabras:
        variaciones = generar_variaciones(palabra)
        for var in variaciones:
            if var not in contraseñas:
                contraseñas.append(var)

    with open(archivo_salida, 'w') as archivo:
        for contraseña in contraseñas:
            archivo.write(contraseña + '\n')

generar_contraseñas(archivo_entrada, archivo_salida)