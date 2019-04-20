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


if __name__ == "__main__":
    mi_coleccion_con_vistas = MiColeccionConVistas()

    print('300 se escribe "{}"'.format(mi_coleccion_con_vistas[300]))

    print('mi_coleccion_con_vistas tiene {} elementos'.format(len(mi_coleccion_con_vistas)))

    if 200 in mi_coleccion_con_vistas:
        print('200 existe en mi_coleccion_con_vistas')
    else:
        print('200 NO existe en mi_coleccion_con_vistas')

    for valor in mi_coleccion_con_vistas:
        print('Elemento de mi_coleccion_con_vistas: {}'.format(valor))

    vista_claves = mi_coleccion_con_vistas.keys()
    print("vista_claves: {}".format(vista_claves))
    for clave in vista_claves:
        print('Clave de mi_coleccion_con_vistas: {}'.format(clave))

    vista_valores = mi_coleccion_con_vistas.values()
    print("vista_valores: {}".format(vista_valores))
    for valor in vista_valores:
        print('Valor de mi_coleccion_con_vistas: {}'.format(valor))

    vista_items = mi_coleccion_con_vistas.items()
    print("vista_items: {}".format(vista_items))
    for item in vista_items:
        print('Ítem de mi_coleccion_con_vistas: {}'.format(item))
