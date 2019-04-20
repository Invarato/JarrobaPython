#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dará el aviso "Unused", pero lo está utilizando eval(), ahí el IDE no analiza el uso y se cree que no se va a usar
from ClaseMisDeportes import MisDeportes


if __name__ == "__main__":
    representacion_evaluada = eval("MisDeportes(['Running', 'Futbol', 'Ciclismo'])")
    representacion_evaluada.add_deporte('Baloncesto')

    print(representacion_evaluada)
