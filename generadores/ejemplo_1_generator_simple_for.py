#!/usr/bin/env python
# -*- coding: utf-8 -*-


def funcion_generadora(ristra_de_cajas):
    for caja in ristra_de_cajas:
        if caja == "BLANCO":
            yield "AZUL"
        elif caja == "ROJO":
            yield "MORADO"
        else:
            yield caja


if __name__ == "__main__":
    ristra_de_cajas = ["BLANCO", "ROJO", "NEGRO"]

    generador = funcion_generadora(ristra_de_cajas)

    for caja_pintada in generador:
        print(caja_pintada)
