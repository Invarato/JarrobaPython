#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Nuestro Servidor Software sobre el Servidor Físico
import socketserver

# Dirección IP
HOST = "85.208.20.119"

# El puerto privado que queramos escuchar, uno de los comprendidos entre 49152 y 65535  1-65535
PORT = 50000


class MiControladorTCP(socketserver.BaseRequestHandler):
    """
    La clase que controlará las peticiones para nuestro servidor.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        """
        Método sobrescrito para controlar la comunicación que ocurra ne nuestro servidor.
        Aquí recibiremos los mensajes del cliente y le responderemos
        """
        print('[Servidor 3] Cliente conectado desde: {}'.format(self.client_address[0]))

        socket_abierto = True
        while socket_abierto:
            print('[Servidor 4] Esperando por petición del cliente...')
            dato_recibido_en_bytes = self.request.recv(1024).strip()
            if dato_recibido_en_bytes:
                dato_recibido_en_str = dato_recibido_en_bytes.decode("utf-8") 
                print('[Servidor 5] Recibido desde el cliente: {}'.format(dato_recibido_en_str))

                respuesta_en_str = "## RESPUESTA DEL SERVIDOR: {} ##".format(dato_recibido_en_str)
                
                self.request.sendall(bytes(respuesta_en_str, encoding='utf8'))
                print('[Servidor 6] Se ha respondido al cliente con el mensaje: {}'.format(respuesta_en_str))
            else:
                print('[Servidor 7] El cliente ha cerrado el Socket desde su lado, cerrando socket desde el Servidor...')
                socket_abierto = False


if __name__ == "__main__":
    tupla_para_el_enlace = (HOST, PORT)

    try:
        print('[Servidor 1] Enlazando Socket en: {}'.format(tupla_para_el_enlace))
        with socketserver.TCPServer(tupla_para_el_enlace, MiControladorTCP) as servidor:
            print('[Servidor 2] Iniciando bucle del servidor. Para interrumpir pulsar a la vez las teclas: [Ctrl]+[C]')
            servidor.serve_forever()
    except KeyboardInterrupt:
        print('[Servidor 8] Interrupción por teclado')
    finally:        
        if servidor is not None:
            servidor.shutdown()
        print('[Servidor 9] Servidor Cerrado')
