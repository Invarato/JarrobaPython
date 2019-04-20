#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    mi_diccionario = {
        "MANZANA": "Manzano",
        "UVA": "Vid",
        "PERA": "Peral",
    }

    vista_claves = mi_diccionario.keys()
    vista_valores = mi_diccionario.values()
    vista_items = mi_diccionario.items()

    # ===========
    print("\n\n")
    print("LAS VIEWS SON SIZED:")
    cantidad_de_claves = len(vista_claves)
    print("Cantidad de claves: {}".format(cantidad_de_claves))

    # ===========
    print("\n\n")
    print("LAS VIEWS SON ITERABLE:")
    for valor in vista_valores:
        print('Valor de mi_diccionario: {}'.format(valor))

    # ===========
    print("\n\n")
    print("KEYSVIEWS ES SET:")
    conjunto_claves = {"MANZANA", "PERA", "TOMATE"}
    conjunto_claves_comunes = vista_claves & conjunto_claves
    print('Conjunto de claves en ambos: {}'.format(conjunto_claves_comunes))

    # ===========
    print("\n\n")
    print("ITEMSVIEWS ES SET:")
    conjunto_tuplas_clave_y_valor = {("MANZANA", "Manzano"), ("TOMATE", "Tomatero")}

    conjunto_items_comunes = vista_items ^ conjunto_tuplas_clave_y_valor
    print('Conjunto de ítems NO en ambos: {}'.format(conjunto_items_comunes))

    # ===========
    print("\n\n")
    print("VALUESVIEWS NO ES SET (PERO SE PUEDE CONVERTIR A SET):")
    conjunto_valores = {"Tomatero", "Vid", "Manzano"}

    # Convertimos la vista en conjunto
    conjunto_de_vista_valores = set(vista_valores)

    conjunto_valores_comunes = conjunto_de_vista_valores & conjunto_valores
    print('Conjunto de valores comunes: {}'.format(conjunto_valores_comunes))

    # ===========
    print("\n\n")
    print("VALUESVIEWS NO ES SET (PERO SE PUEDE CONVERTIR A SET):")
    conjunto_valores = {"Tomatero", "Vid", "Manzano"}

    # ===========
    print("\n\n")
    print("VIEWS ESTÁN ASOCIADAS A SU DICCIONARIO:")

    # Obtenemos una vista; por ejemplo, las claves
    vista_claves = mi_diccionario.keys()

    # Recorremos las claves de dentro de la vista
    for clave in vista_claves:
        print('Clave de mi_diccionario ANTES: {}'.format(clave))

    # Añadimos una clave y un valor que no exista en el diccionario
    mi_diccionario["LIMÓN"] = "Limonero"

    # Volvemos a recorrer las claves dentro de la vista para comprobar
    for clave in vista_claves:
        print('Clave de mi_diccionario DESPUES: {}'.format(clave))
