import socket
import argparse
parser = argparse.ArgumentParser(description="Escanea los puertos dados y reporta su estado")
parser.add_argument("IP", help="Proporciona la IP para escanear")
parser.add_argument("Puertos", help="Ingresa los puertos que desea escanear como una lista separada por comas (Ej: 22,80,443)")
args = parser.parse_args()
ip = args.IP
puertos = [int(p) for p in args.Puertos.split(',')]
for puerto in puertos:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if (s.connect_ex((ip, puerto))==0):
        print ("El puerto num " +str(puerto)+ " esta abierto :)")
        s.settimeout(1)
        s.close()
