#!/usr/bin/env python
# -*- coding: utf-8 -*-


def funcion_generadora_de_numeros_en_texto():
    yield "UNO"
    yield "DOS"
    yield "TRES"
    return


if __name__ == "__main__":
    iterable = funcion_generadora_de_numeros_en_texto()
    try:
        print(next(iterable))
        print(next(iterable))
        print(next(iterable))
        print(next(iterable))
    except StopIteration:
        print("El Generador se ha agotado y ha devuelto StopIteration")
