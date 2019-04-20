#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc


class Medible(abc.Sized):

    def __init__(self):
        self.cantidad_de_letras = 3
        self.texto_con_letras = "ABC"

    def add_letra(self, letra):
        self.texto_con_letras += letra
        self.cantidad_de_letras += 1

    def __len__(self):
        return self.cantidad_de_letras

    def get_texto(self):
        return self.texto_con_letras


if __name__ == "__main__":
    mi_medible = Medible()

    texto = mi_medible.get_texto()
    cantidad_letras_del_texto = len(mi_medible)

    print('mi_medible tiene {} letras en el texto: "{}"'.format(cantidad_letras_del_texto, texto))

    mi_medible.add_letra("D")

    texto = mi_medible.get_texto()
    cantidad_letras_del_texto = len(mi_medible)

    print('mi_medible tiene {} letras en el texto: "{}"'.format(cantidad_letras_del_texto, texto))
