#!/usr/bin/env python
# -*- coding: utf-8 -*-


def funcion_generadora_print():
    try:
        print("GENERADOR: Se va a generar un PRIMER dato")
        yield "valorGenerado1"

        print("GENERADOR: Se va a generar un SEGUNDO dato")
        yield "valorGenerado2"

        print("GENERADOR: Se va a generar un TERCER dato")
        yield "valorGenerado3"
    except GeneratorExit:
        print("GENERADOR: Se ha capturado la excepción GeneratorExit")


if __name__ == "__main__":

    generador = funcion_generadora_print()

    print(next(generador))
    print(next(generador))

    print("Cerrando el generador")
    del generador  # Y el recolector de basura de Python llama a generador.close()
