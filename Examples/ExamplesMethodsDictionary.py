# Carlos Hernandez Navarro
# 10/04/2021
# metodos dicionarios

# metodo get busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto
def ejemplo_get():
    print("Ejemplo metodo get\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    gete = biblitecaejemplo.get('e', 'no existe')
    if biblitecaejemplo.get('a', 'no existe'):
        geta = "existe"
    print(gete, "\n", geta)
    input("\n pulsa enter para continuar...\n")


# metodo keys genera una lista en clave de los registros del diccionario
def ejemplo_keys():
    print("Ejemplo metodo keys\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo values genera una lista en valor de los registros del diccionario
def ejemplo_values():
    print("Ejemplo metodo values\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo items genera una lista en clave-valor de los registros del diccionario.
def ejemplo_items():
    print("Ejemplo metodo items\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo pop extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto
def ejemplo_pop():
    print("Ejemplo metodo pop\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo clear borra todos los registros de un diccionario
def ejemplo_clear():
    print("Ejemplo metodo clear\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo dict recibe como parámetro una representación de un diccionario y si es factible,
# devuelve un diccionario de datos
def ejemplo_dict():
    print("Ejemplo metodo dict\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo zip ecibe como parámetro dos elementos iterables, ya sea una cadena, una lista o una tupla.
# Ambos parámetros deben tener el mismo número de elementos.
# Se devolverá un diccionario relacionando el elemento i-esimo de cada uno de los iterables
def ejemplo_zip():
    print("Ejemplo metodo zip\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo copy retorna una copia del diccionario original
def ejemplo_copy():
    print("Ejemplo metodo copy\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo fromKeys recibe como parámetros un iterable y un valor,
# devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado.
# Si el valor no es ingresado, devolverá none para todas las claves
def ejemplo_fromkeys():
    print("Ejemplo metodo fromKeys\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo setDefault funciona de dos formas. En la primera como get,
# y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.
def ejemplo_setdefault():
    print("Ejemplo metodo setDefault\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo upDate recibe como parámetro otro diccionario. Si se tienen claves iguales,
# actualiza el valor de la clave repetida; si no hay claves iguales,
# este par clave-valor es agregado al diccionario
def ejemplo_update():
    print("Ejemplo metodo upDate\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    print("despues de agregar el elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


def ejemplo_diccionario():
    ejemplo_get()
#    ejemplo_keys()
#    ejemplo_values()
#    ejemplo_items()
#    ejemplo_pop()
#    ejemplo_clear()
#    ejemplo_dict()
#    ejemplo_zip()
#    ejemplo_copy()
#    ejemplo_fromkeys()
#    ejemplo_setdefault()
#    ejemplo_update()


# main
ejemplo_diccionario()
