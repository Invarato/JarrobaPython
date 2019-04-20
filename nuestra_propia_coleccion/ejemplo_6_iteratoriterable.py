#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc


class IteradorIterable(abc.Iterator):

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

    def __iter__(self):
        return self


if __name__ == "__main__":
    mi_iterador_iterable = IteradorIterable()

    for valor in mi_iterador_iterable:
        print('Elemento de mi_iterador_iterable: {}'.format(valor))
