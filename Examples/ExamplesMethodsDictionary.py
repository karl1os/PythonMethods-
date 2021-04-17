# Carlos Hernandez Navarro
# 10/04/2021
# metodos dicionarios


def menuinput():
    print("Menu de ejemplos ")
    print("------------------")
    print("1. metodo get")
    print("2. metodo keys")
    print("3. metodo values")
    print("4. metodo items")
    print("5. metodo pop")
    print("6. metodo clear")
    print("7. metodo dict")
    print("8. metodo zip")
    print("9. metodo copy")
    print("10.metodo fromkeys")
    print("11.metodo setdefault")
    print("12.metodo update")
    print("0. Salir")
    opcion = input("Elije un metodo que quieras mostrar: \n")
    return opcion


# not works, problem whit opcion, is a String, expected integer
def comprovador(opcion):
    if opcion.isnumeric():
        value = int(opcion)
        if value < 13:
            if value >= 0:
                validador = True
                return validador
            else:
                validador = False
                return validador
        else:
            validador = False
            return validador
    else:
        print("Has intriducido una opcion invalida\n")
        menumain()


def menufunc(opcion):
    values = int(opcion)
    if values == 1:
        ejemplo_get()
    elif values == 2:
        ejemplo_keys()
    elif values == 3:
        ejemplo_values()
    elif values == 4:
        ejemplo_items()
    elif values == 5:
        ejemplo_pop()
    elif values == 6:
        ejemplo_clear()
    elif values == 7:
        ejemplo_dict()
    elif values == 8:
        ejemplo_zip()
    elif values == 9:
        ejemplo_copy()
    elif values == 10:
        ejemplo_fromkeys()
    elif values == 11:
        ejemplo_setdefault()
    elif values == 12:
        ejemplo_update()


def menumain():
    opcionvalida = True
    while opcionvalida:
        opcion = menuinput()
        opcionvalida = comprovador(opcion)
        if int(opcion) == 0:
            exit()
        elif opcionvalida:
            menufunc(opcion)


# metodo get busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto
def ejemplo_get():
    geta = None
    print("Ejemplo metodo get\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    gete = biblitecaejemplo.get('e', 'no existe')
    if biblitecaejemplo.get('a', 'no existe'):
        geta = "existe"
    print("metodo get con el indice e: ", gete, "\n", "metodo get con el indice a: ", geta, "\n")
    input("\n pulsa enter para continuar...\n")


# metodo keys genera una lista en clave de los registros del diccionario
def ejemplo_keys():
    print("Ejemplo metodo keys: \n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    keys = biblitecaejemplo.keys()
    print("\nClaves del diccionario bibliotecaejemplo: \n", keys, "\n")
    input("\n pulsa enter para continuar...\n")


# metodo values genera una lista en valor de los registros del diccionario
def ejemplo_values():
    print("Ejemplo metodo values\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    values = biblitecaejemplo.values()
    print("\nValores del diccionario bibliotecaejemplo: \n", values)
    input("\n pulsa enter para continuar...\n")


# metodo items genera una lista en clave-valor de los registros del diccionario.
def ejemplo_items():
    print("Ejemplo metodo items\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    clavesvalor = biblitecaejemplo.items()
    print("los valores del diccionario son: \n", clavesvalor)
    input("\n pulsa enter para continuar...\n")


# metodo pop extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto
def ejemplo_pop():
    print("Ejemplo metodo pop\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    biblitecaejemplo.pop("b")
    print("despues de eliminar un elemento:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo clear borra todos los registros de un diccionario
def ejemplo_clear():
    print("Ejemplo metodo clear\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    print("Dicionario original", biblitecaejemplo)
    biblitecaejemplo.clear()
    print("Despues de limpiar el dicionario:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo dict recibe como parámetro una representación de un diccionario y si es factible,
# devuelve un diccionario de datos
def ejemplo_dict():
    print("Ejemplo metodo dict\n")
    print("mediante este metodo comprovamos si los datos que agregamos son correctos, si es asi crea un diccionario\n")
    biblitecaejemplo = dict(a="1", b="2", c="3", d="4")
    print("Dicionario creado", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo zip ecibe como parámetro dos elementos iterables, ya sea una cadena, una lista o una tupla.
# Ambos parámetros deben tener el mismo número de elementos.
# Se devolverá un diccionario relacionando el elemento i-esimo de cada uno de los iterables
def ejemplo_zip():
    print("Ejemplo metodo zip\n")
    print("crea un diccionario a partir de dos grupos de datos, deben tener el mismo numero de elementos\n")
    biblitecaejemplo = dict(zip("abcd", [1, 2, 3, 4]))
    print("Dicionario creado", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo copy retorna una copia del diccionario original
def ejemplo_copy():
    print("Ejemplo metodo copy\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    biblitecaejemplo2 = biblitecaejemplo.copy()
    print("Dicionario original", biblitecaejemplo)
    print("Dicionario copiado", biblitecaejemplo2)
    input("\n pulsa enter para continuar...\n")


# metodo fromKeys recibe como parámetros un iterable y un valor,
# devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado.
# Si el valor no es ingresado, devolverá none para todas las claves
def ejemplo_fromkeys():
    print("Ejemplo metodo fromKeys\n")
    biblitecaejemplo = dict.fromkeys(["a", "b", "c", "d"], 1)
    print("Dicionario creado", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# metodo setDefault funciona de dos formas. En la primera como get,
# y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.
def ejemplo_setdefault():
    print("Ejemplo metodo setDefault")
    print("modo get: \n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    valor = biblitecaejemplo.setdefault("b")
    print("valor extraido: ", valor, "\n")
    print("en modo agregar elemento\n")
    valor2 = biblitecaejemplo.setdefault("e", "5")
    print("despues de agregar el elemento:", biblitecaejemplo, " elemento agregado ", valor2)
    input("\n pulsa enter para continuar...\n")


# metodo upDate recibe como parámetro otro diccionario. Si se tienen claves iguales,
# actualiza el valor de la clave repetida; si no hay claves iguales,
# este par clave-valor es agregado al diccionario
def ejemplo_update():
    print("Ejemplo metodo upDate\n")
    biblitecaejemplo = {"a": "1", "b": "2", "c": "3", "d": "4"}
    biblitecaejemplo2 = {"c": 6, "b": 5, "e": 9, "f": 10}
    print("Dicionario original", biblitecaejemplo)
    biblitecaejemplo.update(biblitecaejemplo2)
    print("despues de actualizar la biblioteca:", biblitecaejemplo)
    input("\n pulsa enter para continuar...\n")


# main
menumain()
