#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    def mi_funcion(var_de_func):
        print("var_de_func (id: {}): {}".format(id(var_de_func), var_de_func))
        var_de_func += ["añadido"]
        print("var_de_func antes de retornar (id: {}): {}".format(id(var_de_func), var_de_func))
        return var_de_func

    mi_variable_mutable = ["algo", "algo más"]
    print("mi_variable_mutable (id: {}): {}".format(id(mi_variable_mutable), mi_variable_mutable))

    retorno_de_funcion = mi_funcion(mi_variable_mutable)
    print("retorno_de_funcion (id: {}): {}".format(id(retorno_de_funcion), retorno_de_funcion))

    print("mi_variable_mutable después de función (id: {}):\t.\t{}".format(id(mi_variable_mutable), mi_variable_mutable))
