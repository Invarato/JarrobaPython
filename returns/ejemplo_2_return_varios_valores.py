#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dame_un_tupla():
    return ("Texto", True, 123)


def dame_varios_valores():
    return "Texto", True, 123


def dame_varios_valores_en_una_tupla():
    # Suponemos que estas variables vienen de un proceso más complicado
    primer_valor = "Texto"
    segundo_valor = True
    tercer_valor = 123

    # Normalmente se pone junto al return, pero quiero que se vea claro que esta
    # manera de declarar la tupla para luego utilizar estos valores fuera de la función
    mi_tupla = primer_valor, segundo_valor, tercer_valor

    return mi_tupla


if __name__ == "__main__":
    print(dame_un_tupla())
    print(dame_varios_valores())

    print(dame_varios_valores_en_una_tupla())

    tupla_devuelta = dame_varios_valores_en_una_tupla()
    primer_valor = tupla_devuelta[0]
    segundo_valor = tupla_devuelta[1]
    tercer_valor = tupla_devuelta[2]
    print("1 primer_valor: {}, segundo_valor: {}, tercer_valor: {}".format(primer_valor,
                                                                           segundo_valor,
                                                                           tercer_valor))

    primer_valor, segundo_valor, tercer_valor = tupla_devuelta
    print("2 primer_valor: {}, segundo_valor: {}, tercer_valor: {}".format(primer_valor,
                                                                           segundo_valor,
                                                                           tercer_valor))

    primer_valor, segundo_valor, tercer_valor = dame_varios_valores_en_una_tupla()
    print("3 primer_valor: {}, segundo_valor: {}, tercer_valor: {}".format(primer_valor,
                                                                           segundo_valor,
                                                                           tercer_valor))
