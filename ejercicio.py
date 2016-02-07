#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open("/etc/passwd","r");
lineas = fd.readlines()
fd.close()
diccionario = {}
keys = [ "root", "imaginario"]
for linea in lineas:
    if not linea:
        break
    corte = linea.split(':')
    login = corte[0]
    shell = corte[-1]
    diccionario[login] = shell[:-1]
for key in keys:
    encontrado = key in diccionario
    if encontrado != 0:
        print key + ":", diccionario[key]
    else:
        print key + ": No encontrado"
