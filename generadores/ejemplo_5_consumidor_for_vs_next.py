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

    print("\n===========")
    print("==CON FOR==")
    generador = funcion_generadora_prints()
    for elemento in generador:
        print(elemento)

    print("\n============")
    print("==CON NEXT==")
    generador = funcion_generadora_prints()
    try:
        valor_generado = next(generador)
        print("Valor generador y obtenido desde el generador: {}".format(valor_generado))

        valor_generado = next(generador)
        print("Valor generador y obtenido desde el generador: {}".format(valor_generado))

        valor_generado = next(generador)
        print("Valor generador y obtenido desde el generador: {}".format(valor_generado))

        # Nuestro generador solo puede generar tres valores, por lo que llamar una cuarta vez a next lanza la excepción StopIteration
        valor_generado = next(generador)
        print("Valor generador y obtenido desde el generador: {}".format(valor_generado))
    except StopIteration:
        print("EXCEPCIÓN StopIteration: El Generador ya ha generado todos los valores posibles")



