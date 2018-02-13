#!/usr/bin/python3

import sys

def suma(op1,op2):
    return op1+op2
def resta(op1,op2):
    return op1-op2
def multiplicacion(op1,op2):
    return op1*op2
def division(op1,op2):
    try:
        return op1/op2
    except ZeroDivisionError:
        return("No puedes dividir entre 0")

funciones = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division
}

if __name__ == "__main__":
    NUM_ARGS = 4

    if len(sys.argv) != NUM_ARGS:
        sys.exit("usage : [num1][operador][num2]")
    
    try:
        operador = sys.argv[2]
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[3])
    except IndexError:
        sys.exit("usage : [num1][operador][num2]")
    except ValueError:
        sys.exit("comprobar que el operando 1 y el operando 2 son numericos")

    try:
        resultado = funciones[operador](num1,num2)
    except KeyError:
        sys.exit("No existe la funcion "+ operador)
    print(resultado)
    

