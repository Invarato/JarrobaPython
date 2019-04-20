#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import abc


class Contenedor(abc.Container):

    def __contains__(self, x):
        if x == 'algo':
            return True
        else:
            return False


if __name__ == "__main__":
    mi_contenedor = Contenedor()

    if "algo" in mi_contenedor:
        print('Existe en mi_contenedor')
    else:
        print('NO existe en mi_contenedor')
