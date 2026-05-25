# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:43:05 2026

@author: SantiagoAlejandroMor
"""

# functools se importa cuando necesitas herramientas para trabajar con funciones de orden superior


# funcion normal 
def saludar():
    print("Hola!")
    
# Imprimir "---" antes y despues

def decorador(func):
    def wrapper():
        print("---")
        func()
        print("---")
    return wrapper

@decorador
def saludar():
    print("Hola")

saludar()
    
registry = []
def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func
@register
def f1():
    print("running f1()")

f1()
for i in registry:
    print(i)
    
# Acceder a variables globales y locales
b = 6 
def print_number(a):
    global b
    print(a)
    print(b)
    b =9
print_number(3)