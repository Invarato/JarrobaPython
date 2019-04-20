#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MisDeportes(object):

    def __init__(self):
        self.listado_deportes = []

    def add_deporte(self, deporte: str):
        self.listado_deportes.append(deporte)

    def __str__(self) -> str:
        str_con_el_resultado = 'Objeto de deportes: '
        for deporte in self.listado_deportes:
            str_con_el_resultado += "\n  * {}".format(deporte)
        return str_con_el_resultado


if __name__ == "__main__":
    mis_deportes = MisDeportes()

    mis_deportes.add_deporte('Running')
    mis_deportes.add_deporte('Futbol')
    mis_deportes.add_deporte('Ciclismo')

    print(mis_deportes)

    print("\n\n")
    print("ES LO MISMO QUE USAR str():")
    representacion_para_humanos = str(mis_deportes)
    print(representacion_para_humanos)
