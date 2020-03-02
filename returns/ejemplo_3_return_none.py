#!/usr/bin/env python
# -*- coding: utf-8 -*-


def traduce_a_ingles(palabra_espanol):
    diccionario_espanol_ingles = {
        "casa": "house",
        "tarta": "cake"
    }

    try:
        return diccionario_espanol_ingles[palabra_espanol]
    except KeyError:
        return None


if __name__ == "__main__":
    palabra_en_ingles = traduce_a_ingles("casa")
    print("casa = {}".format(palabra_en_ingles))

    palabra_en_ingles = traduce_a_ingles("habitación")
    print("habitación = {}".format(palabra_en_ingles))
