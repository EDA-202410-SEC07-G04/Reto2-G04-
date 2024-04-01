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
from datetime import datetime as dt
import sys
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

    catalog['countries'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.99)

    catalog['companies'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.99)
    """
    catalog['info'] = mp.newMap(259837,
                                maptype='CHAINING',
                                loadfactor=1)

    catalog['multilocations'] = mp.newMap(244937,
                                          maptype='CHAINING',
                                          loadfactor=0.99)
    
    catalog['skills'] = mp.newMap(577166,
                                  maptype='CHAINING',
                                  loadfactor=0.99)
    """
    return catalog

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass

def newId(pubid):
    entry = {'ide': "", "jobs": None}
    entry["ide"] = pubid
    entry["jobs"] = lt.newList("SINGLE_LINKED", compareDate)
    return entry

def addJob(catalog, job):
    try:
        jobs = catalog['jobs']
        if (job['id'] != ''):
            pubid = job['id']
            pubid = str(pubid)
        else:
            pubid = " "
        existid = mp.contains(jobs, pubid)
        if existid:
            entry = mp.get(jobs, pubid)
            ide = me.getValue(entry)
        else:
            ide = newId(pubid)
            mp.put(jobs, pubid, ide)
        lt.addLast(ide['jobs'], job)
    except Exception:
        return None

def newCountrycode(pubccode):
    entry = {'Countrycode': "", "jobs": None}
    entry["Countrycode"] = pubccode
    entry["jobs"] = lt.newList("SINGLE_LINKED", compareDate)
    return entry

def addCountrycode(catalog, job):
    try:
        jobs = catalog['countries']
        if (job['country_code'] != ''):
            pubccode = job['country_code']
            pubccode = str(pubccode)
        else:
            pubccode = " "
        existid = mp.contains(jobs, pubccode)
        if existid:
            entry = mp.get(jobs, pubccode)
            Ccode = me.getValue(entry)
        else:
            Ccode = newCountrycode(pubccode)
            mp.put(jobs, pubccode, Ccode)
        lt.addLast(Ccode['jobs'], job)
    except Exception:
        return None

def newCompanyname(pubname):
    entry = {'companyname': "", "jobs": None}
    entry["companyname"] = pubname
    entry["jobs"] = lt.newList("SINGLE_LINKED")
    return entry

def addCompanyname(catalog, job):
    try:
        jobs = catalog['companies']
        if (job['company_name'] != ''):
            pubname = job['company_name'].lower()
            pubname = str(pubname.lower())
        else:
            pubname = " "
        existid = mp.contains(jobs, pubname.lower())
        if existid:
            entry = mp.get(jobs, pubname.lower())
            Cname = me.getValue(entry)
        else:
            Cname = newCompanyname(pubname.lower())
            mp.put(jobs, pubname.lower(), Cname)
        lt.addLast(Cname['jobs'], job)
    except Exception:
        return None

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

def get_subi(data_structs):
    
    pass

def req_1(data_structs, n_ofertas, cod_pais, xp):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    lt1 = lt.newList("ARRAY_LIST")
    country = mp.get(data_structs['countries'], cod_pais)
    if country:
        var1 = me.getValue(country)['jobs']
        cant_of_pais = mp.size(var1)
        for i in lt.iterator(var1):
            if xp.lower() == i["experience_level"].lower():
                lt.addLast(lt1, i)
    
    if lt.size(lt1) == 0:
        print("Ningun resultado encontrado")
        sys.exit(0)
    elif n_ofertas > lt.size(lt1):
        n_ofertas = lt.size(lt1)
    elif n_ofertas <= lt.size(lt1):
        n_ofertas = n_ofertas 

    final = lt.subList(lt1, 0, n_ofertas)

    cant_xp = lt.size(lt1)

    return final, cant_xp, cant_of_pais


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
    ltjr = lt.newList("ARRAY_LIST")
    ltm = lt.newList("ARRAY_LIST")
    ltsr = lt.newList("ARRAY_LIST")
    chili = lt.newList("ARRAY_LIST")
    
    company = mp.get(data_structs['companies'], nom_empresa)
    #print(company)
    if company:
        var1 = me.getValue(company)['jobs']
        for i in lt.iterator(var1):
            fecha_diccionario = dt.strptime(i["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
            fecha_diccionario_dt = fecha_diccionario.strftime("%Y-%m-%d")
            if fecha_inicial_dt <= fecha_diccionario_dt and fecha_diccionario_dt <= fecha_final_dt:
                if "junior" == i["experience_level"].lower():
                    lt.addLast(ltjr, i)
                elif "mid" == i["experience_level"].lower():
                    lt.addLast(ltm, i)
                elif "senior" == i["experience_level"].lower():
                    lt.addLast(ltsr, i)
                lt.addLast(chili, i)
    

    if lt.size(chili) >= 2:
        sortiao = merg.sort(chili, sort_r3)
    elif lt.size(chili) <= 1:
        sortiao = chili 

    #Bitfinex
    #intelligints

    if lt.isEmpty(chili):
        print("Ningun resultado encontrado")
        sys.exit(0)

    cant_of = lt.size(chili)
    cant_xp_jr = lt.size(ltjr)
    cant_xp_m = lt.size(ltm)
    cant_xp_sr = lt.size(ltsr)

    return sortiao, cant_of, cant_xp_jr, cant_xp_m, cant_xp_sr

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


def sort_r3(oferta1, oferta2):
    date1 = dt.strptime(oferta1['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    date2 = dt.strptime(oferta2['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    name1 = oferta1['country_code']
    name2 = oferta2['country_code']
    if date1 > date2:
        return True
    elif date1 == date2:
        if name1 < name2:
            return True
        else:
            return False
    else:
        return False

def compareDate():
    pass