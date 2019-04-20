#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc
import random


class MiHashable(abc.Hashable):

    def __init__(self):
        self.valor_guardado = None

        salt = random.random()
        tupla_de_parametros_de_mi_clase = (salt, self.valor_guardado)
        self.codigo_hash_del_objeto = hash(tupla_de_parametros_de_mi_clase)

    def set_valor(self, valor):
        self.valor_guardado = valor

    def get_valor(self):
        return self.valor_guardado

    def __hash__(self):
        return self.codigo_hash_del_objeto


if __name__ == "__main__":
    mi_objeto_x = MiHashable()
    mi_objeto_y = MiHashable()

    print('Hash de mi_objeto_x: {}'.format(hash(mi_objeto_x)))
    print('Hash de mi_objeto_y: {}'.format(hash(mi_objeto_y)))

    mi_objeto_x.set_valor("Un valor")
    mi_objeto_y.set_valor("Otro valor diferente")

    print('Hash de mi_objeto_x después de modificar el estado: {}'.format(hash(mi_objeto_x)))
    print('Hash de mi_objeto_y después de modificar el estado: {}'.format(hash(mi_objeto_y)))
