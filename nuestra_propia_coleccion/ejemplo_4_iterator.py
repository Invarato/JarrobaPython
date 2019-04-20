#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc


class Iterador(abc.Iterator):

    def __init__(self):
        self.siguiente_valor_a_devolver = 0

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


if __name__ == "__main__":
    mi_iterador = Iterador()

    try:

        # PRIMERO
        str_val_conv = mi_iterador.__next__()
        print('__next__ devuelve: "{}"'.format(str_val_conv))

        # SEGUNDO
        str_val_conv = mi_iterador.__next__()
        print('__next__ devuelve: "{}"'.format(str_val_conv))

        # TERCERO
        str_val_conv = mi_iterador.__next__()
        print('__next__ devuelve: "{}"'.format(str_val_conv))

        # StopIteration
        str_val_conv = mi_iterador.__next__()
        print('No llega a este print por la excepcion StopIteration: "{}"'.format(str_val_conv))

    except StopIteration:
        print('La ultima llamada a __next__ ha lanzado la excepcion StopIteration')
