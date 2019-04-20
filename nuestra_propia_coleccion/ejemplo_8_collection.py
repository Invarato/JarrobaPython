#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc


class MiColeccionIterador(abc.Collection, abc.Iterator):

    def __init__(self):
        self.siguiente_valor_a_devolver = 0

    def __len__(self):
        return 3

    def __contains__(self, x):
        return x is "PRIMERO" or x is "SEGUNDO" or x is "TERCERO"

    def __next__(self):
        self.siguiente_valor_a_devolver += 1

        if self.siguiente_valor_a_devolver == 1:
            return "PRIMERO"
        elif self.siguiente_valor_a_devolver == 2:
            return "SEGUNDO"
        elif self.siguiente_valor_a_devolver == 3:
            return "TERCERO"
        else:
            raise StopIteration

    def __iter__(self):
        self.siguiente_valor_a_devolver = 0
        return self


if __name__ == "__main__":

    mi_coleccion_iterador = MiColeccionIterador()

    print('mi_coleccion_iterador tiene {} elementos'.format(len(mi_coleccion_iterador)))

    if "ALGO" in mi_coleccion_iterador:
        print('"ALGO" Existe en mi_coleccion_iterador')
    else:
        print('"ALGO" NO existe en mi_coleccion_iterador')

    if "SEGUNDO" in mi_coleccion_iterador:
        print('"SEGUNDO" Existe en mi_coleccion_iterador')
    else:
        print('"SEGUNDO" NO existe en mi_coleccion_iterador')

    for valor in mi_coleccion_iterador:
        print('Elemento de mi_coleccion_iterador: {}'.format(valor))
