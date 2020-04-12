#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    generador = (num * 10 for num in range(1000000000))

    for numero in generador:
        print(numero)
