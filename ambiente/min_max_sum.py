# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

from random import randint

def Min_max_sum():
    # Generate five random positive integers
    numeros_inteiros_lista = [randint(1, 100) for i in range(5)]
    print(numeros_inteiros_lista)

    numeros_inteiros_lista.sort()
    print(numeros_inteiros_lista)

    minimo = sum(numeros_inteiros_lista[:4])
    maximo = sum(numeros_inteiros_lista[1:])
    return minimo, maximo

result = Min_max_sum()
print(result)

