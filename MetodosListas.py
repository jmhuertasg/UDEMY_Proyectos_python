lista = ["Tomate","Cebolla","Huevos","Leche", "Arroz"]
lista2 = [1, 2, 3, 4, 5]
lista3 = [6, 7, 8, 9, 10]
lista4 = ['d', 'f', 'a', 'b', 'e', 'c']

#agregar a una lista
lista.append(50)
print(lista)

del lista[3]
print(lista)

lista2.extend(lista3)
print(lista2)

lista.remove('Arroz')
print(lista)

lista4.sort()
print(lista4)