#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MisDeportes(object):

    def __init__(self):
        self.listado_deportes = []

    def add_deporte(self, deporte: str):
        self.listado_deportes.append(deporte)


if __name__ == "__main__":
    mis_deportes = MisDeportes()

    mis_deportes.add_deporte('Running')
    mis_deportes.add_deporte('Futbol')
    mis_deportes.add_deporte('Ciclismo')

    print(mis_deportes)
