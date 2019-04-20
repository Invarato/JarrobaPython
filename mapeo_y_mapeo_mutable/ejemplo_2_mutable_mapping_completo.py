#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc
from typing import Iterator


class MiDiccionarioEspecialDeDulces(abc.MutableMapping,
                                    abc.Iterator):

    def __init__(self, *args, cosas_que_no_son_dulces: set = None, **kwargs):

        self.diccionario_de_dulces_con_sus_calorias = {}
        self.cosas_que_no_son_dulces = set()

        self.nuevo_conjunto_de_cosas_que_no_son_dulces(cosas_que_no_son_dulces)

        self.update(dict(*args, **kwargs))

        self.lista_ordenada_de_nombres_de_pasteles = None

    def nuevo_conjunto_de_cosas_que_no_son_dulces(self, cosas_que_no_son_dulces: set = None) -> None:
        """
        Método que sustituye al conjunto anterior y comprueba que todos los elementos del listado cumplan con que sean dulces
        :param cosas_que_no_son_dulces: set de valores de tipo str con las cosas que no son dulces
        :return: None
        """
        if cosas_que_no_son_dulces is None:
            self.cosas_que_no_son_dulces = set()
        else:
            self.cosas_que_no_son_dulces = cosas_que_no_son_dulces

        # Comprobación que no se cuele nada que no sea dulce en el diccionario de dulces
        conjunto_de_claves_dulces = set(self.diccionario_de_dulces_con_sus_calorias.keys())
        conjunto_algo_no_dulce_entre_las_claves = conjunto_de_claves_dulces & self.cosas_que_no_son_dulces
        for clave_no_valida in conjunto_algo_no_dulce_entre_las_claves:
            print('Se ha eliminado "{}" porque no es un dulce'.format(clave_no_valida))
            del self.diccionario_de_dulces_con_sus_calorias[clave_no_valida]

    def __getitem__(self, clave: str) -> int:
        try:
            calorias_del_pastel = self.diccionario_de_dulces_con_sus_calorias[clave]
            return calorias_del_pastel
        except KeyError:
            raise KeyError("Este Contenedor no tiene la clave '{}'".format(clave))

    def __setitem__(self, clave: str, valor: int) -> None:
        if clave in self.cosas_que_no_son_dulces:
            print('Se ha descartado "{}" porque no es un dulce'.format(clave))
        else:
            self.diccionario_de_dulces_con_sus_calorias[clave] = valor

    def __delitem__(self, clave: str) -> None:
        try:
            del self.diccionario_de_dulces_con_sus_calorias[clave]
        except KeyError:
            raise KeyError("Este Contenedor no tiene la clave '{}'".format(clave))

    def __len__(self) -> int:
        cantidad_de_dulces = len(self.diccionario_de_dulces_con_sus_calorias)
        return cantidad_de_dulces

    def __next__(self) -> str:
        if self.lista_ordenada_de_nombres_de_pasteles is None:
            lista_nombres_pasteles_desordenado = self.diccionario_de_dulces_con_sus_calorias.keys()
            self.lista_ordenada_de_nombres_de_pasteles = sorted(lista_nombres_pasteles_desordenado)

        try:
            return self.lista_ordenada_de_nombres_de_pasteles.pop(0)
        except IndexError:
            raise StopIteration

    def __iter__(self) -> Iterator[str]:
        self.lista_ordenada_de_nombres_de_pasteles = None
        return self

    def __repr__(self):
        return '{self.__class__.__name__}({self.diccionario_de_dulces_con_sus_calorias}, cosas_que_no_son_dulces={self.cosas_que_no_son_dulces})'.format(
            self=self)

    def __str__(self):
        str_con_el_resultado = ''
        for nombre_del_pastel, calorias_del_pastel in self.diccionario_de_dulces_con_sus_calorias.items():
            str_con_el_resultado += "\n  * {} tiene {} calorías.".format(nombre_del_pastel, calorias_del_pastel)
        return str_con_el_resultado


if __name__ == "__main__":

    print("RECONSTRUIMOS NUESTRO OBJETO MUTABLE MAPPING DESDE EL CONSTRUCTOR:")
    mi_segundo_diccionario_de_dulces = MiDiccionarioEspecialDeDulces({'Caramelo': 147,
                                                                      'Piruleta': 269,
                                                                      'MESA': 10000000},
                                                                     cosas_que_no_son_dulces={'SILLA',
                                                                                              'MESA'})

    for clave in mi_segundo_diccionario_de_dulces:
        print('Clave de mi_diccionario_de_dulces: {}'.format(clave))

    # ==========
    print("\n\n")
    print("CONSTRUIMOS NUESTRO OBJETO PARA PROBAR LOS EJEMPLOS:")

    mi_diccionario_de_dulces = MiDiccionarioEspecialDeDulces()
    cosas_que_no_son_dulces = {
        "TELEVISION",
        "FLOR",
        "MARTILLO",
        "LAPIZ",
        "RELOJ"
    }
    mi_diccionario_de_dulces.nuevo_conjunto_de_cosas_que_no_son_dulces(cosas_que_no_son_dulces)
    mi_diccionario_de_dulces["Tortita"] = 227
    mi_diccionario_de_dulces["Gofre"] = 291
    mi_diccionario_de_dulces["Galleta"] = 488
    mi_diccionario_de_dulces["Torrija"] = 229
    mi_diccionario_de_dulces["Tarta"] = 372
    mi_diccionario_de_dulces["Magdalena"] = 377
    mi_diccionario_de_dulces["Croissant"] = 466
    mi_diccionario_de_dulces["MARTILLO"] = 1000000

    # ==========
    print("\n\n")
    print("REPRESENTACIÓN DE NUESTRO MUTABLE MAPPING PARA DEPURAR:")
    print(repr(mi_diccionario_de_dulces))

    # ==========
    print("\n\n")
    print("REPRESENTACIÓN DE NUESTRO MUTABLE MAPPING PARA QUE SEA LEGIBLE:")
    print(mi_diccionario_de_dulces)

    # ==========
    print("\n\n")
    print("USO DE LAS VISTAS DE NUESTRO MUTABLE MAPPING:")
    vista_claves = mi_diccionario_de_dulces.keys()
    print("vista_claves: {}".format(vista_claves))
    for clave in vista_claves:
        print('Clave de mi_diccionario_de_dulces: {}'.format(clave))

    vista_valores = mi_diccionario_de_dulces.values()
    print("vista_valores: {}".format(vista_valores))
    for valor in vista_valores:
        print('Valor de mi_diccionario_de_dulces: {}'.format(valor))

    vista_items = mi_diccionario_de_dulces.items()
    print("vista_items: {}".format(vista_items))
    for item in vista_items:
        print('Item de mi_diccionario_de_dulces: {}'.format(item))

    # ==========
    print("\n\n")
    print("ITERADOR ITERABLE (HEMOS HECHO QUE EN __next__ DEVUELVA EN ORDEN ALFABÉTICO LAS CLAVES):")
    for clave in mi_diccionario_de_dulces:
        print('Clave de mi_diccionario_de_dulces: {}'.format(clave))
