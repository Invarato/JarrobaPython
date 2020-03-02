#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dame_un_texto():
    return "Texto"


def dame_un_numero():
    return 123


def dame_un_booleano():
    return True


def dame_un_listado():
    return ["A", "B", "C"]


def dame_un_diccionario():
    return {
        "casa": "house",
        "tarta": "cake"
    }


def dame_un_none():
    return None


if __name__ == "__main__":
    valor = dame_un_texto()
    print(valor)

    print(dame_un_numero())
    print(dame_un_booleano())
    print(dame_un_listado())
    print(dame_un_diccionario())

    print(dame_un_none())
