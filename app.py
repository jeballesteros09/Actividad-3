from pymongo import MongoClient

# Inicializacion de Base de Datos
mongo_url = "mongodb://localhost:27017"
mongo_db = MongoClient(mongo_url)

# print(mongo_db.list_database_names())

# Crear base de datos
db = mongo_db["diccionario"]

# Crear coleccion


collection = db.get_collection("Palabras")

if collection is None:
    collection = db.create_collection("Palabras")
else:
    pass

data = dict()
data_1 = dict()


def inicio():
    menu()


def menu():
    print("Elija una opcion: "
          "\n1- Agregar palabra"
          "\n2- Editar palabra"
          "\n3- Eliminar palabra"
          "\n4- Ver listado de palabras"
          "\n5- Buscar significado de palabras"
          "\n6- Salir")

    opcion = int(input("Opcion: "))

    if opcion == 1:
        agregar_palabra()
    elif opcion == 2:
        editar_palabra()
    elif opcion == 3:
        eliminar_palabra()
    elif opcion == 4:
        ver_palabras()
    elif opcion == 5:
        buscar_palabra()
    elif opcion == 6:
        exit(0)
    else:
        print("Ingrese valores enteros del 1 al 5.")
        inicio()


def agregar_palabra():
    palabra = input("Ingrese palabra: ")
    significado = input("Ingrese significado: ")
    data = {"Palabra": palabra, "Significado": significado}
    x = collection.insert_one(data).inserted_id
    inicio()


def editar_palabra():
    palabra = input("Ingrese palabra a modificar: ")
    nuevo = input("Ingrese nuevo significado: ")
    valor = {"$set": {"Significado": nuevo}}
    q = {"Palabra": palabra}
    collection.update_one(q, valor)
    inicio()


def eliminar_palabra():
    filtro = input("Ingrese palabra a eliminar: ")
    data_1["Palabra"] = filtro
    collection.delete_one(data_1)
    inicio()


def ver_palabras():
    documentos = collection.find()
    for documento in documentos:
        print(documento)
    inicio()


def buscar_palabra():
    filtro = input("Ingrese palabra a buscar: ")
    data_1["Palabra"] = filtro
    documento = collection.find_one(data_1)
    print(documento)
    inicio()


inicio()
