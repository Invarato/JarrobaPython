#!/usr/bin/env python
# -*- coding: utf-8 -*-


def funcion_generadora_prints():
    print("GENERADOR: Se va a generar un PRIMER dato")
    yield "valorGenerado1"

    print("GENERADOR: Se va a generar un SEGUNDO dato")
    yield "valorGenerado2"

    print("GENERADOR: Se va a generar un TERCER dato")
    yield "valorGenerado3"

    print("GENERADOR: Termina y lanzará automáticamente la excepción StopIteration")



if __name__ == "__main__":
    generador = funcion_generadora_prints()
    try:
        primer_valor = next(generador)
        segundo_valor = next(generador)
        tercer_valor = next(generador)

        # Nuestro generador solo puede generar tres valores, por lo que llamar una cuarta vez a next lanza la excepción StopIteration
        cuarto_valor = next(generador)
    except StopIteration:
        print("El Generador ya ha generado todos los valores posibles")
