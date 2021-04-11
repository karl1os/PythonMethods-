# Carlos Hernandez Navarro
# 08/03/2021


# metodo append, este agrega un elemento en la ultima posicion de la lista
def ejemplo_append():
    print("Ejemplo append\n")
    lista_append = [1, 2, 3]
    print("Lista original", lista_append)
    lista_append.append(7)
    print("despues de agregar el elemento:", lista_append)
    input("\n pulsa enter para continuar...\n")


# metodo clear, este limpia una lista dejandola vacia
def ejemplo_clear():
    print("Ejemplo clear\n")
    lista_clear = [4, 5, 6]
    print("Lista original", lista_clear)
    lista_clear.clear()
    print("Despues de limpiar la lista")
    input("\n pulsa enter para continuar...\n")


# metodo extend, este une dos listas en una
def ejemplo_extend():
    print("Ejemplo extend\n")
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    print("Listas originales", lista1, lista2)
    lista1.extend(lista2)
    print("Despues de aplicar el metodo", lista1)
    input("\n pulsa enter para continuar...\n")


# metodo count, cuenta el numero de veces que aparece un item
def ejemplo_count():
    print("Ejemplo count\n")
    lista_count = [1, 2, 3, 1, 4, 5, 1]
    print("Lista original", lista_count)
    print(lista_count.count(1))
    input("\n pulsa enter para continuar...\n")


# metodo index, devuelve el indice en el que aparece un item
def ejemplo_index():
    print("Ejemplo index\n")
    lista_index = [1, 2, 3, 4, 5, 6]
    print("Lista original", lista_index, " buscaremos el numero 4")
    print(lista_index.index(4))
    input("\n pulsa enter para continuar...\n")


# metodo insert, agrega un item a la lista en un indice especifico
def ejemplo_insert():
    print("Ejemplo insert\n")
    lista_insert = [1, 2, 3]
    print("Lista original", lista_insert)
    lista_insert.insert(4, 4)  # tambien puede ser posicion negativa partiendo de la ultima posicion que sera 0, y si pones uno fuera del rango se posicionara en la ultima posicion.
    print("Despues de insertar en la lista", lista_insert)
    input("\n pulsa enter para continuar...\n")


# metodo pop, extrae un item de la lista y lo borra, si no especificas la posicion eliminara el ultimo (LIFO last in first out).
def ejemplo_pop():
    print("Ejemplo pop\n")
    lista_pop = [1, 2, 3, 4, 5, 6]
    print("Lista original", lista_pop)
    lista_pop.pop(4)
    print("Despues de eliminar un elemento", lista_pop)
    input("\n pulsa enter para continuar...\n")


# metodo remove, borra el primer elemento de la lista cuyo valor concuerde con el que indicamos
def ejemplo_remove():
    print("Ejemplo remove\n")
    lista_remove = [0, 2, 3, 1, 4, 5, 1]
    print("Lista original", lista_remove)
    lista_remove.remove(1)  # debemos comprovar si existe para evitar problemas.
    print("Despues de eliminar un elemento", lista_remove)
    input("\n pulsa enter para continuar...\n")


# metodo reverse, le da la vuelta a la lista actual
def ejemplo_reverse():
    print("Ejemplo reverse\n")
    lista_reverse = [1, 2, 3]
    print("Lista original", lista_reverse)
    lista_reverse.reverse()
    print("Despues de voltear la lista", lista_reverse)
    input("\n pulsa enter para continuar...\n")


# metodo sort, ordena automaticamente los items de una lista por su valor de menor a mayor
def ejemplo_sort():
    print("Ejemplo sort\n")
    lista_sort = [1, 3, 6, 2, 4, 8, 5, 7, 0]
    print("Lista original", lista_sort)
    lista_sort.sort()  # si ordenamos string lo hara mediante el codigo asci y caracter a caracter, por lo que ordenara por char.
    print("Despues de ordenar la lista", lista_sort)
    input("\n pulsa enter para continuar...\n")


# metodo sorted
def ejemplo_sorted():
    print("Ejemplo sorted\n")
    lista_sorted = [1, 3, 6, 2, 4, -8, 5, 7, 0]
    print("Lista original", lista_sorted)
    x = sorted(lista_sorted)
    print("Despues de pasar por el metodo", lista_sorted)
    print("Lista creada por el metodo sorted", x)
    input("\n pulsa enter para continuar...\n")


def ejemplo_copy():
    print("Ejemplo copy\n")
    lista_copy = [1, 3, 6, 2, 4, 8, 5, 7, 0]
    print("Lista original", lista_copy)
    lista_copy2 = lista_copy.copy()
    print("Lista original y copiada", lista_copy, lista_copy2)
    input("\n pulsa enter para continuar...\n")


def ejemplo_lista():
    ejemplo_append()  #
    ejemplo_clear()  #
    ejemplo_extend()  #
    ejemplo_count()  #
    ejemplo_index()  #
    ejemplo_insert()  #
    ejemplo_pop()  #
    ejemplo_remove()  #
    ejemplo_reverse()
    ejemplo_sort()  #
    ejemplo_sorted()  #
    ejemplo_copy()  #


# main
ejemplo_lista()
