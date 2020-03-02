#!/usr/bin/env python
# -*- coding: utf-8 -*-


def busca(cosa_a_buscar):
    listado_cosas = ["boligrafo", "taza", "cuchara"]

    for cosa in listado_cosas:
        if cosa == cosa_a_buscar:
            print("Encontrado")
            return

    print("No encontrado")
    return  # El return vacío al final de la declaración de la función se puede omitir


if __name__ == "__main__":
    busca("taza")
    busca("armario")
