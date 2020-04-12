#!/usr/bin/env python
# -*- coding: utf-8 -*-


def funcion_generadora_contador_infinito(valor_a_sumar):
    acumulado = 0
    while True:
        acumulado += valor_a_sumar
        nuevo_valor_a_sumar = yield acumulado

        # Es importante comprobar el valor devuelto en el yield, ya que si solo se tira sin llamar a send devolverá None
        if nuevo_valor_a_sumar is not None:
            valor_a_sumar = nuevo_valor_a_sumar


if __name__ == "__main__":

    valor_de_inicio_a_sumar = 1
    generador = funcion_generadora_contador_infinito(valor_de_inicio_a_sumar)

    valor_generado = next(generador)
    print("ANTES   valor generado: {}".format(valor_generado))
    valor_generado = next(generador)
    print("ANTES   valor generado: {}".format(valor_generado))

    # Cuando queramos usamos send, que devolverá un valor al igual que next, ya que se envía el valor al generador y busca el siguiente yield
    nuevo_valor_a_sumar_y_enviar = 10
    valor_generado = generador.send(nuevo_valor_a_sumar_y_enviar)
    print("ENVIAR  valor generado: {}".format(valor_generado))

    valor_generado = next(generador)
    print("DESPUES valor generado: {}".format(valor_generado))
    valor_generado = next(generador)
    print("DESPUES valor generado: {}".format(valor_generado))
