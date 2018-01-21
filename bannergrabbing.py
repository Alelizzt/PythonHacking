import socket
import sys

# Socket de tivpo ipv4 con protocolo tcp
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Recorriendo las maquinas
for host in range(80,100):
    ports = open('ports.txt','r')
    vulbanners = open('vulbanners.txt','r')
    # Recorriendo los puertos
    for port in ports:
        try:
            # Abriendo conexion a los host con el segmento de red (sys.argv[1]) proporcionado por el usuario en la linea de comandos
            socket.connect(( str(sys.argv[1]+srt(host)), int(port) ))
            print('Connecting to '+str(sys.argv[1]+'-'+srt(host))+' in the port: '+str(port))
            socket.settimeout(1)
            # Capturando el banner que retorna el servidor
            banner = socket.recv(1024)
            for vulbanner in vulbanners:
                if banner.strip() in vulbanner.strip():
                    print ('We have a winner! '+banner)
                    print ('Host: '+str(sys.argv[1]+'-'+str(host)))
                    print('Port: '+str(port))
        except:
            # print ('Error connecting to: '+str(sys.argv[1]+'-'+srt(host))+' in the port: '+str(port))
            pass
