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


class Iterable(abc.Iterable):

    def __iter__(self):
        mmi_iterador = Iterador()
        return mmi_iterador


if __name__ == "__main__":
    print('Bucle “for” normal:')
    mi_lista = [1, 2, 3, 4, 5]

    for valor in mi_lista:
        print('Elemento de mi_ lista: {}'.format(valor))

    print('\n\n')
    print('Simular el interior de un bucle “for”:')
    mi_iterable = Iterable()
    mi_iterador = mi_iterable.__iter__()

    continuar = True
    while continuar:
        try:
            valor = mi_iterador.__next__()
            print('__next__ devuelve: "{}"'.format(valor))
        except StopIteration:
            print('La ultima llamada a __next__ ha lanzado la excepcion StopIteration, que sirve para salir del bucle WHILE')
            continuar = False
