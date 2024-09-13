from scapy.all import *
import socket
import argparse
def escanear_puerto_syn(ip, puerto):
    paquete = IP(dst=ip)/TCP(dport=puerto, flags="S")
    respuesta = sr1(paquete, timeout=1, verbose=0)
    if respuesta is None:
        return "Filtrado"
    elif respuesta.haslayer(TCP):
        if respuesta.getlayer(TCP).flags == 0x12: # SYN-ACK
            send(IP(dst=ip)/TCP(dport=puerto, flags="R"), verbose=0)
            return "Abierto"
        elif respuesta.getlayer(TCP).flags==0x14: # RST-ACK
            return "Cerrado"
    return "Desconocido"
parser = argparse.ArgumentParser(description="Escanea los puertos dados y reporta su estado")
parser.add_argument("IP", help="Proporciona la IP para escanear")
parser.add_argument("Puertos", help="Ingresa los puertos que desea escanear como una lista separada por comas (Ej: 22,80,443)")
args = parser.parse_args()
ip = args.IP
puertos = [int(p) for p in args.Puertos.split(',')]
for puerto in puertos:
    estado = escanear_puerto_syn(ip, puerto)
    print(f"El puerto {puerto} está {estado}")
##    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##    if (s.connect_ex((ip, i))==0):
##        print ("El puerto num " +repr(i)+ " esta abierto :)")
##        s.settimeout(1)
##        s.close()
##    s.close()