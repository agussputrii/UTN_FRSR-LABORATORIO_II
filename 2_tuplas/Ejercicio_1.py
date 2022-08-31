tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for i in range(len(tupla)):
    if tupla[i] < 5:
        lista.append(tupla[i]) # Agrega los elementos menores a 5 a la lista

print(lista) 