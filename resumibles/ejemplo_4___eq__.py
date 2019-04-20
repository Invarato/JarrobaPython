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

    def __hash__(self) -> int:
        return self.codigo_hash_del_objeto

    def __eq__(self, otro_objeto):
        valor_del_otro_objeto = otro_objeto.get_valor()
        return valor_del_otro_objeto == self.valor_guardado


if __name__ == "__main__":
    print("SI TIENEN EL DIFERENTE VALOR GUARDADO LOS DOS OBJETOS:")
    mi_objeto_x = MiHashable()
    mi_objeto_y = MiHashable()

    # Si tienen diferentes valores guardados los objetos
    mi_objeto_x.set_valor("Un valor")
    mi_objeto_y.set_valor("Otro valor diferente")

    if mi_objeto_x == mi_objeto_y:
        print("El contenido de mi_objeto_x es igual que el de mi_objeto_y")
    else:
        print("El contenido de mi_objeto_x NO es igual que el de mi_objeto_y")

    del mi_objeto_x
    del mi_objeto_y

    print("\n\n")
    print("SI TIENEN EL MISMO VALOR GUARDADO LOS DOS OBJETOS:")

    mi_objeto_x = MiHashable()
    mi_objeto_y = MiHashable()

    # O si tienen el mismo valor guardado los dos objetos
    mi_objeto_x.set_valor("El mismo valor")
    mi_objeto_y.set_valor("El mismo valor")

    if mi_objeto_x == mi_objeto_y:
        print("El contenido de mi_objeto_x es igual que el de mi_objeto_y")
    else:
        print("El contenido de mi_objeto_x NO es igual que el de mi_objeto_y")
