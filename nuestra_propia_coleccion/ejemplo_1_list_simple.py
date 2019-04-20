#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    mi_listado = ['PRIMERO', 'SEGUNDO', 'TERCERO']

    # Es Medible
    cantidad_elementos = len(mi_listado)
    print('Cantidad de elementos en mi_listado: {}'.format(cantidad_elementos))

    # Es Contenedor
    if "SEGUNDO" in mi_listado:
        print('Existe en mi_listado')
    else:
        print('NO existe en mi_listado')

    # Es Iterable
    for valor in mi_listado:
        print('Elemento del listado: {}'.format(valor))
