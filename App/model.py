"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
data_struct = None

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos

    catalog = {'info': None,
               'jobs': None,
               'multilocations': None,
               'skills': None}

    catalog['jobs'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.99)
    catalog['info'] = mp.newMap(259837,
                                maptype='CHAINING',
                                loadfactor=1)
    catalog['multilocations'] = mp.newMap(244937,
                                          maptype='CHAINING',
                                          loadfactor=0.99)
    
    catalog['skills'] = mp.newMap(577166,
                                  maptype='CHAINING',
                                  loadfactor=0.99)
    
    return catalog

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, n_ofertas, cod_pais, xp):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    lt1 = lt.newList("ARRAY_LIST")
    lt2 = lt.newList("ARRAY_LIST")
    cant_xp = 0
    cant_of_pais = 0
    for i in data_structs: 
        if cod_pais.lower() == data_structs:
            lt.addFirst(lt1, data_structs)
            if xp == data_structs:
                lt.addLast(lt2, data_structs)

    
    if lt.size(lt2) == 0:
        print("Ningun resultado encontrado")
        sys.exit(0)
    elif n_ofertas > lt.size(lt2):
        n_ofertas = lt.size(lt2)
    elif n_ofertas <= lt.size(lt2):
        n_ofertas = n_ofertas 

    final = lt.subList(lt2, 0, n_ofertas)

    for x in lt.iterator(lt2):
        cant_xp += 1

    for j in lt.iterator(lt1):
        cant_of_pais += 1

    
    return final, cant_xp, cant_of_pais

    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs, nom_empresa, fecha_inicial_consulta, fecha_final_consulta):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    fecha_inicial_dt = str(dt.strptime(fecha_inicial_consulta, "%Y-%m-%d"))
    fecha_final_dt = str(dt.strptime(fecha_final_consulta, "%Y-%m-%d"))
    chili = lt.newList("ARRAY_LIST")
    for i in range(1, data_structs):
        fecha_diccionario = dt.strptime(lt.getElement(data_structs["jobs"], i)["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
        fecha_diccionario_dt = fecha_diccionario.strftime("%Y-%m-%d")
        if nom_empresa.lower() == data_structs:
            if fecha_inicial_dt <= fecha_diccionario_dt and fecha_diccionario_dt <= fecha_final_dt:
                lt.addLast(chili, i)
                if lt.size(chili) >= 2:
                    sortiao = merg.sort(chili, sort_r3)
                elif lt.size(chili) <= 1:
                    sortiao = chili 

    if lt.isEmpty(chili):
        print("Ningun resultado encontrado")
        sys.exit(0)

    return sortiao

    pass


def req_4(data_structs, cod_pais, fecha_inicial_consulta, fecha_final_consulta):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    chili = lt.newList("ARRAY_LIST")
    fecha_inicial_dt = str(dt.strptime(fecha_inicial_consulta, "%Y-%m-%d"))
    fecha_final_dt = str(dt.strptime(fecha_final_consulta, "%Y-%m-%d")) 
    for i in range(1, data_structs):
        fecha_diccionario = dt.strptime(lt.getElement(data_structs["jobs"], i)["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
        fecha_diccionario_dt = fecha_diccionario.strftime("%Y-%m-%d")
        if i["country_code"] == cod_pais: 
            if fecha_inicial_dt <= fecha_diccionario_dt and fecha_diccionario_dt <= fecha_final_dt:
                lt.addLast(chili, i)
                if lt.size(chili) >= 2:
                    sortiao = merg.sort(chili, sort_r3)
                elif lt.size(chili) <= 1:
                    sortiao = chili 

    if lt.isEmpty(chili):
        print("Ningun resultado encontrado")
        sys.exit(0)
    
    return sortiao 
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass


def sort_r3():
    pass