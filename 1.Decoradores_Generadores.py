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


# Decoradores con 


## Closures

class Averager():
    def __init__ (self):
        self.series = []
    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)
avg = Averager()
avg(12)

### Decorador con parametros 3 funciones 
import time
def reintentar (veces =3, delay=1.0): # Capa de parametros
    def decorador(func):                # Capa que recibe la funcion
        def wrapper(*args,**kwargs):    # Capa que se ejecuta para cada llamada
            for i in range(veces):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"intenti {i+1} fallo: {e}")
                    if i == veces -1:
                        raise
                    time.sleep(delay)
        return wrapper 
    return decorador

fabrica = reintentar(veces = 3, delay=0.5)
print(fabrica)
def llamar_api(url):
    print(f"llamando {url}...")
    raise Exception("sin conexión")
decorada = fabrica(llamar_api)
print(decorada)
decorada("http://ejemplo.com")



