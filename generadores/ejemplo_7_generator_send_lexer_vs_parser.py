#!/usr/bin/env python
# -*- coding: utf-8 -*-


def funcion_generadora_lexer(texto):
    articulos = {"el", "los", "la", "las", "un", "unos", "una", "unas"}
    preposiciones = {"a", "ante", "bajo", "cabe",
                     "con", "contra", "de", "desde",
                     "en", "entre", "hacia", "hasta",
                     "para", "por", "según", "sin", "so",
                     "sobre", "tras"}

    sujeto_o_verbo = "sujeto"

    palabras = texto.lower().split(" ")
    for palabra in palabras:
        if palabra in articulos:
            nuevo_sujeto_o_verbo = yield palabra, "artículo"
        elif palabra in preposiciones:
            nuevo_sujeto_o_verbo = yield palabra, "preposición"
        else:
            nuevo_sujeto_o_verbo = yield palabra, sujeto_o_verbo

        if nuevo_sujeto_o_verbo is not None:
            sujeto_o_verbo = nuevo_sujeto_o_verbo


if __name__ == "__main__":

    texto = "Juan come pan de la panadería"

    generador = funcion_generadora_lexer(texto)

    for palabra, tipo in generador:
        print("La palabra '{}' es de tipo '{}'".format(palabra, tipo))

        try:
            if tipo == "artículo":
                palabra, tipo = generador.send("sujeto")
                print("La palabra '{}' es de tipo '{}'".format(palabra, tipo))

            if tipo == "sujeto":
                palabra, tipo = generador.send("verbo")
                print("La palabra '{}' es de tipo '{}'".format(palabra, tipo))

            if tipo == "verbo":
                palabra, tipo = generador.send("sujeto")
                print("La palabra '{}' es de tipo '{}'".format(palabra, tipo))
        except StopIteration:
            pass
