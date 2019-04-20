#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc


class MiColeccionConVistas(abc.Mapping):

    def __init__(self, *args, **kwargs):
        self.lista_interna_claves = [100, 200, 300]
        self.lista_interna_valores = ["CIEN", "DOSCIENTOS", "TRESCIENTOS"]

    def __len__(self) -> int:
        return 3

    def __iter__(self):
        return iter(self.lista_interna_claves)

    def __getitem__(self, numero: int) -> str:
        try:
            posicion = self.lista_interna_claves.index(numero)
            return self.lista_interna_valores[posicion]
        except ValueError:
            raise KeyError

    def __repr__(self):
        dict_claves_y_valores = dict(self.items())
        return '{self.__class__.__name__}({dict_claves_y_valores})'.format(self=self, dict_claves_y_valores=dict_claves_y_valores)


if __name__ == "__main__":
    mi_coleccion_con_vistas = MiColeccionConVistas()

    vista_claves = mi_coleccion_con_vistas.keys()
    print("vista_claves: {}".format(vista_claves))

    vista_valores = mi_coleccion_con_vistas.values()
    print("vista_valores: {}".format(vista_valores))

    vista_items = mi_coleccion_con_vistas.items()
    print("vista_items: {}".format(vista_items))
