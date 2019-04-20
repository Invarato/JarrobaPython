#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    print("SI LOS OBJETOS DEVUELVEN DIFERENTE IDENTIDAD:")
    mi_objeto_a = "Un texto"
    mi_objeto_b = "Otro texto"

    print("Identidad de mi_objeto_a: {}".format(id(mi_objeto_a)))
    print("Identidad de mi_objeto_b: {}".format(id(mi_objeto_b)))

    if mi_objeto_a is mi_objeto_b:
        print("La identidad de mi_objeto_a es igual que la de mi_objeto_b")
    else:
        print("La identidad de mi_objeto_a NO es igual que la de mi_objeto_b")

    del mi_objeto_a
    del mi_objeto_b
    # =====================

    print("\n\n")
    print("SI LOS OBJETOS DEVUELVEN LA MISMA IDENTIDAD:")
    mi_objeto_a = "Un texto"
    mi_objeto_b = mi_objeto_a

    print("entidad de mi_objeto_a: {}".format(id(mi_objeto_a)))
    print("entidad de mi_objeto_b: {}".format(id(mi_objeto_b)))

    if mi_objeto_a is mi_objeto_b:
        print("La identidad de mi_objeto_a es igual que la de mi_objeto_b")
    else:
        print("La identidad de mi_objeto_a NO es igual que la de mi_objeto_b")

    del mi_objeto_a
    del mi_objeto_b
    # =====================

    print("\n\n")
    print("VALORES DE LOS OBJETOS IGUALES QUE APUNTAN EN MEMORIA AL PRIMERO DECLARADO:")
    mi_objeto_a = "Un texto"
    mi_objeto_b = "Un texto"

    print("entidad de mi_objeto_a: {}".format(id(mi_objeto_a)))
    print("entidad de mi_objeto_b: {}".format(id(mi_objeto_b)))

    if mi_objeto_a is mi_objeto_b:
        print("La identidad de mi_objeto_a es igual que la de mi_objeto_b")
    else:
        print("La identidad de mi_objeto_a NO es igual que la de mi_objeto_b")

    del mi_objeto_a
    del mi_objeto_b
    # =====================

    print("\n\n")
    print("VALORES DE LOS OBJETOS IGUALES QUE APUNTAN EN MEMORIA AL PRIMERO DECLARADO QUE CAMBIA DE PUNTERO DE MEMORIA AL CAMBIAR SU VALOR:")

    mi_objeto_a = "Un texto"
    mi_objeto_b = "Un texto"

    print("[Antes] entidad de mi_objeto_a: {}".format(id(mi_objeto_a)))
    print("[Antes] entidad de mi_objeto_b: {}".format(id(mi_objeto_b)))

    mi_objeto_b += " y algo más"

    print("[Despues] entidad de mi_objeto_a: {}".format(id(mi_objeto_a)))
    print("[Despues] entidad de mi_objeto_b: {}".format(id(mi_objeto_b)))

    if mi_objeto_a is mi_objeto_b:
        print("La identidad de mi_objeto_a es igual que la de mi_objeto_b")
    else:
        print("La identidad de mi_objeto_a NO es igual que la de mi_objeto_b")