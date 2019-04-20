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
    mi_iterable = Iterable()

    for valor in mi_iterable:
        print('Elemento de mi_iterable: {}'.format(valor))
