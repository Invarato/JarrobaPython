#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc
from typing import Iterator


class MiDiccionarioEspecialDeDulces(abc.MutableMapping):

    def __init__(self):
        self.diccionario_de_dulces_con_sus_calorias = {}
        self.cosas_que_no_son_dulces = set()

        # Nota: se inicializa un conjunto vacío con “set()” y no con “{}” porque sin inicializar con “valores” o “claves y valores” Python lo interpreta siempre como conjunto

    def __len__(self) -> int:
        cantidad_de_dulces = len(self.diccionario_de_dulces_con_sus_calorias)
        return cantidad_de_dulces

    def __iter__(self) -> Iterator[str]:
        iterador_de_dulces = self.diccionario_de_dulces_con_sus_calorias.__iter__()
        return iterador_de_dulces

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

    def __getitem__(self, clave: str) -> int:
        try:
            calorias_del_pastel = self.diccionario_de_dulces_con_sus_calorias[clave]
            return calorias_del_pastel
        except KeyError:
            raise KeyError("Este Contenedor no tiene la clave '{}'".format(clave))

    def nuevo_conjunto_de_cosas_que_no_son_dulces(self, cosas_que_no_son_dulces: set) -> None:
        # Si nos cuelan un None en el parámetro cosas_que_no_son_dulces lo traduciremos como conjunto vacío set()
        if cosas_que_no_son_dulces is None:
            self.cosas_que_no_son_dulces = set()
        else:
            self.cosas_que_no_son_dulces = cosas_que_no_son_dulces

        # Al añadir un nuevo conjunto de cosas que nos son dulces nos interesa comprobar que no se hubiera colado nada que no se un dulce con anterioridad, por lo que lo comprobamos
        conjunto_de_claves_dulces = set(self.diccionario_de_dulces_con_sus_calorias.keys())
        conjunto_algo_no_dulce_entre_las_claves = conjunto_de_claves_dulces & self.cosas_que_no_son_dulces
        for clave_no_valida in conjunto_algo_no_dulce_entre_las_claves:
            print('Se ha eliminado "{}" porque no es un dulce'.format(clave_no_valida))
            del self.diccionario_de_dulces_con_sus_calorias[clave_no_valida]
        # Los valores que sean iguales en el conjunto_de_claves_dulces y (&) en el conjunto self.cosas_que_no_son_dulces serán las cosas que no son dulces que se han colado y hay que eliminarlo


if __name__ == "__main__":
    # Instanciación de nuestro diccionario personalizado
    mi_diccionario_de_dulces = MiDiccionarioEspecialDeDulces()

    # Conjunto con las cosas que no son dulces
    cosas_que_no_son_dulces = {
        "TELEVISION",
        "FLOR",
        "MARTILLO",
        "LAPIZ",
        "RELOJ"
    }

    # Añadimos el conjunto de cosas que no son dulces a nuestro diccionario personalizado
    mi_diccionario_de_dulces.nuevo_conjunto_de_cosas_que_no_son_dulces(cosas_que_no_son_dulces)

    # Añadir elementos a nuestro diccionario personalizado
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
    print("ITERAR POR TODAS LAS CLAVES:")
    for clave in mi_diccionario_de_dulces:
        print('Clave de mi_diccionario_de_dulces: {}'.format(clave))

    # ==========
    print("\n\n")
    print("ELIMINAR UNA CLAVE Y VOLVER A ITERAR PARA COMPROBAR QUE SE HA ELIMINADO:")
    del mi_diccionario_de_dulces["Tarta"]
    for clave in mi_diccionario_de_dulces:
        print('Clave de mi_diccionario_de_dulces: {}'.format(clave))

    # ==========
    print("\n\n")
    print("COMPROBAR SI EXISTE UNA CLAVE:")
    if "Gofre" in mi_diccionario_de_dulces:
        print('La clave "Gofre" EXISTE')
    else:
        print('La clave "Gofre" NO EXISTE')

    # ==========
    print("\n\n")
    print("OBTENER VALOR DADO UNA CLAVE QUE EXISTE:")
    valor = mi_diccionario_de_dulces["Gofre"]
    print('Valor obtenido con la clave "Gofre" de mi_diccionario_de_dulces: {}'.format(valor))

    # ==========
    print("\n\n")
    print("COMPROBAR SI NO EXISTE UNA CLAVE:")
    if "Donut" in mi_diccionario_de_dulces:
        print('La clave "Donut" EXISTE')
    else:
        print('La clave "Donut" NO EXISTE')

    # ==========
    print("\n\n")
    print("OBTENER VALOR DADO UNA CLAVE QUE QUIZÁS NO EXISTE:")
    try:
        valor = mi_diccionario_de_dulces["Donut"]
        print('Valor obtenido con la clave "Donut" de mi_diccionario_de_dulces: {}'.format(valor))
    except KeyError as err:
        print('Error devuelto: {}'.format(err))

    # ==========
    print("\n\n")
    print("AÑADIR Y OBTENER VALOR DADO UNA CLAVE QUE QUIZÁS NO EXISTE:")
    mi_diccionario_de_dulces["Donut"] = 452
    try:
        valor = mi_diccionario_de_dulces["Donut"]
        print('Valor obtenido con la clave "Donut" de mi_diccionario_de_dulces: {}'.format(valor))
    except KeyError as err:
        print('Error devuelto: {}'.format(err))
