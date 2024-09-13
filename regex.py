import re 
patron1 = r'[A-Z][a-z]{2,} [A-Z][a-z]{2,}'
patron2=r'@[\w_]+'
patron3=r'(.*([a-zA-Z]+).*(\d+).*)|(.*(\d+).*([a-zA-Z]+).*)'
result=re.search(patron1, 'Juan Legorreta aprobó su examen')
if result:
    print (result.group())
result2=re.search(patron2, 'Mi nombre de usuario es: @juanchoheh_13')
if result2:
    print (result2.group())
result3=re.search (patron3, '.{}@4a')
if result3:
    print (result3.group())