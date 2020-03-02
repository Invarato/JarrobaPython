#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pinta_de_azul(color):
    if color == "BLANCO":
        return "AZUL"
    elif color == "AMARILLO":
        return "VERDE"
    elif color == "ROJO":
        return "MORADO"
    else:
        return None


def esta_en_la_fiesta(persona_a_buscar):
    listado_personas_en_la_fiesta = ["Paco", "María", "Juan"]

    for persona in listado_personas_en_la_fiesta:
        if persona == persona_a_buscar:
            return True

    return False


if __name__ == "__main__":
    print(pinta_de_azul("AMARILLO"))
    print(pinta_de_azul("COLOR QUE NO EXISTE"))

    print(esta_en_la_fiesta("María"))
    print(esta_en_la_fiesta("Rodrigo"))
