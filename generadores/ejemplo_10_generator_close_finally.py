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
    finally:
        print("GENERADOR: Terminando y limpiando")


if __name__ == "__main__":

    generador = funcion_generadora_print()

    for elemento in generador:
        print(elemento)
