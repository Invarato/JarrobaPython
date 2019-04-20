#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    mi_variable_mutable = ["valor 1", "valor 2"]
    print("mi_variable_mutable (id: {}): {}".format(id(mi_variable_mutable), mi_variable_mutable))

    mi_variable_mutable_copiado = list(mi_variable_mutable)
    print("mi_variable_mutable_copiado (id: {}): {}".format(id(mi_variable_mutable_copiado), mi_variable_mutable_copiado))
