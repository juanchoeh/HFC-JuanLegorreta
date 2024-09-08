import xml.etree.ElementTree as ET
import datetime
import hashlib
def obten_hora_inicio(xml):
    with open (xml, 'r') as archivo :
        root=ET.fromstring(archivo.read())
        hora_inicio=datetime.datetime.fromtimestamp(int(root.get('start')))
    return hora_inicio

def obten_hosts_prendidos(xml):
    hosts_encendidos=0
    with open (xml, 'r') as archivo:
        root=ET.fromstring(archivo.read())
        for host in root.findall('host'):
            if host.find('status').get('state')=='up':
                hosts_encendidos += 1
    return hosts_encendidos

def obten_hosts_apagados(xml):
    hosts_apagados=0
    with open (xml, 'r') as archivo:
        root=ET.fromstring(archivo.read())
        for host in root.findall('host'):
            if host.find('status').get('state')=='down':
                hosts_apagados += 1
    return hosts_apagados

def obten_puertos_abiertos(xml, portid):
    puertos_abiertos = 0
    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())
        for host in root.findall('host'):
            ports = host.find('ports')
            if ports is not None: 
                for port in ports.findall('port'):
                    state = port.find('state')
                    if port.get('portid') == portid and state is not None and state.get('state') == 'open':
                        puertos_abiertos += 1
    return puertos_abiertos

def obten_servicios(xml, product):
    http = 0
    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())
        for host in root.findall('host'):
            ports = host.find('ports')
            if ports is not None: 
                for port in ports.findall('port'):
                    servicio=port.find('service')
                    if servicio is not None:
                        producto = servicio.get('product')
                        if producto == product:
                            http += 1
    return http

def calcula_hash (xml):
    hash_md5=hashlib.md5()
    hash_sha1=hashlib.sha1()
    with open (xml, 'rb') as archivo:
        root=archivo.read()
        hash_md5.update(root)
        hash_sha1.update(root)
    return hash_md5.hexdigest(), hash_sha1.hexdigest()


def resultados_fin ():
    hora=obten_hora_inicio('nmap.xml')
    host_prendidos=obten_hosts_prendidos('nmap.xml')
    host_apagados=obten_hosts_apagados('nmap.xml')
    ports22=obten_puertos_abiertos('nmap.xml', '22')
    ports53=obten_puertos_abiertos('nmap.xml', '53')
    ports80=obten_puertos_abiertos('nmap.xml', '80')
    ports443=obten_puertos_abiertos('nmap.xml', '443')
    x, y = calcula_hash('nmap.xml')
    http_apache=obten_servicios('nmap.xml', 'Apache httpd')
    http_honeypot=obten_servicios('nmap.xml', 'Dionaea Honeypot httpd')
    http_nginx=obten_servicios('nmap.xml', 'nginx')
    
    with open ('archivo.txt', 'w') as archivo:
        archivo.write(f"La hora de ejecución fue: {hora}\n")
        archivo.write(f"Los hosts encendidos son: {host_prendidos}\n")
        archivo.write(f"Los hosts apagados son: {host_apagados}\n")
        archivo.write(f"Los hosts con puerto 22 encendidos son: {ports22}\n")
        archivo.write(f"Los hosts con puerto 53 encendidos son: {ports53}\n")
        archivo.write(f"Los hosts con puerto 80 encendidos son: {ports80}\n")
        archivo.write(f"Los hosts con puerto 443 encendidos son: {ports443}\n")
        archivo.write(f"Los que usan Apache son: {http_apache}\n")
        archivo.write(f"Hay estos honeypots: {http_honeypot}\n")
        archivo.write(f"Los que usan Nginx son: {http_nginx}\n")
        archivo.write(f"El hash MD5 es: {x}\n")
        archivo.write(f"El hash SHA1 es: {y}")
    return archivo

resultados_fin()

print(obten_hora_inicio('nmap.xml'))
print(obten_hosts_prendidos('nmap.xml'))
print(obten_hosts_apagados('nmap.xml'))
print(obten_puertos_abiertos('nmap.xml', '22'))
print(obten_puertos_abiertos('nmap.xml', '53'))
print(obten_puertos_abiertos('nmap.xml', '80'))
print(obten_puertos_abiertos('nmap.xml', '443'))