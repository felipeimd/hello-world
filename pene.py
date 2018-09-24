# -*- coding: utf-8 -*-
"""
Pene maravilloso para probar. 
xD
"""

print("HOLA!\nCómo estás oyem??")
print("Yo soy el señor don doctor profesor cirujano")
print("Partamos con lo básico.")

cont = 0
r = input("Eres un chico, o una chica??")
while r not in  ["chico", "chica", "otro"]:
    print("oe no po! di lo que corresponde")
    r = input("Eres un chico, o una chica??")
    cont += 1
    if cont > 3: print("Si no te identificas, puedes poner 'otro' como respuesta")

print("ouh, así que eres un %s"), r
print("Weno, eso era todo, chao!")