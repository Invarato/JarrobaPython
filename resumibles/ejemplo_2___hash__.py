#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MiClase(object):

    def __init__(self):
        self.valor_guardado = None

    def set_valor(self, valor):
        self.valor_guardado = valor


if __name__ == "__main__":
    mi_objeto_x = MiClase()
    mi_objeto_y = MiClase()

    print('Hash de mi_objeto_x: {}'.format(hash(mi_objeto_x)))
    print('Hash de mi_objeto_y: {}'.format(hash(mi_objeto_y)))
