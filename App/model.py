﻿"""
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
from collections import defaultdict
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

    catalog['jobs'] = lt.newList("ARRAY_LIST")

    """catalog['jobs'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.9)"""
    
    catalog['countries'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.9)

    catalog['companies'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.9)

    catalog['cities'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.9)
    
    catalog['xps'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.9)

    catalog['years'] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=0.9)

    
    catalog['info'] = mp.newMap(259837,
                                maptype='CHAINING',
                                loadfactor=0.9)
    """
    catalog['multilocations'] = mp.newMap(244937,
                                          maptype='CHAINING',
                                          loadfactor=0.99)
    
    catalog['skills'] = mp.newMap(577166,
                                  maptype='CHAINING',
                                  loadfactor=0.99)
    """
    
    return catalog


#Funciones carga de datos

def get_jobs_sublist(data_structs):

    ofertas = data_structs["jobs"]
    lista1 = lt.newList("ARRAY_LIST")
    lista0 = lt.newList("ARRAY_LIST")
    sublista1=lt.subList(ofertas,1,3)
    sublista2= lt.subList(ofertas,lt.size(ofertas)-2,3)
    for cada_elem in lt.iterator(sublista1):
       
       dict0 = {}
       dict0["title"] = cada_elem["title"]
       dict0["published_at"] = cada_elem["published_at"]
       dict0["company_name"] = cada_elem["company_name"]
       dict0["experience_level"] = cada_elem["experience_level"]
       dict0["country_code"] = cada_elem["country_code"]
       dict0["city"] = cada_elem["city"]
       lt.addLast(lista0,dict0)
    for elem in lt.iterator(sublista2):
       
       dict1 = {}
       dict1["title"] = elem["title"]
       dict1["published_at"] = elem["published_at"]
       dict1["company_name"] = elem["company_name"]
       dict1["experience_level"] = elem["experience_level"]
       dict1["country_code"] = elem["country_code"]
       dict1["city"] = elem["city"]
       lt.addLast(lista1, dict1)
       
   
       
    return lista1, lista0


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
    jobi = catalog['jobs']
    lt.addLast(jobi, job)
    return catalog

"""def addJob(catalog, job):
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
        return None"""

def newCountrycode(pubccode):
    entry = {'Countrycode': "", "jobs": None}
    entry["Countrycode"] = pubccode
    entry["jobs"] = lt.newList("SINGLE_LINKED", compareDate)
    return entry

def addCountrycode(catalog, job):
    try:
        jobs = catalog['countries']
        if (job['country_code'] != ''):
            pubccode = job['country_code'].lower()
            pubccode = str(pubccode.lower())
        else:
            pubccode = " "
        existid = mp.contains(jobs, pubccode.lower())
        if existid:
            entry = mp.get(jobs, pubccode.lower())
            Ccode = me.getValue(entry)
        else:
            Ccode = newCountrycode(pubccode.lower())
            mp.put(jobs, pubccode.lower(), Ccode)
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

def newCityname(pubcity):
    entry = {'cityname': "", "jobs": None}
    entry["cityname"] = pubcity
    entry["jobs"] = lt.newList("SINGLE_LINKED")
    return entry

def addCityname(catalog, job):
    try:
        jobs = catalog['cities']
        if (job['city'] != ''):
            pubcity = job['city'].lower()
            pubcity = str(pubcity.lower())
        else:
            pubcity = " "
        existid = mp.contains(jobs, pubcity.lower())
        if existid:
            entry = mp.get(jobs, pubcity.lower())
            Cname = me.getValue(entry)
        else:
            Cname = newCityname(pubcity.lower())
            mp.put(jobs, pubcity.lower(), Cname)
        lt.addLast(Cname['jobs'], job)
    except Exception:
        return None

def newXpname(pubxp):
    entry = {'xpname': "", "jobs": None}
    entry["xpname"] = pubxp
    entry["jobs"] = lt.newList("SINGLE_LINKED")
    return entry

def addXpname(catalog, job):
    try:
        jobs = catalog['xps']
        if (job['experience_level'] != ''):
            pubxp = job['experience_level'].lower()
            pubxp = str(pubxp.lower())
        else:
            pubxp = " "
        existxp = mp.contains(jobs, pubxp.lower())
        if existxp:
            entry = mp.get(jobs, pubxp.lower())
            Xname = me.getValue(entry)
        else:
            Xname = newCityname(pubxp.lower())
            mp.put(jobs, pubxp.lower(), Xname)
        lt.addLast(Xname['jobs'], job)
    except Exception:
        return None

def newYear(pubyear):
    entry = {'year': "", "jobs": None}
    entry["year"] = pubyear
    entry["jobs"] = lt.newList("SINGLE_LINKED")
    return entry

def convercioni(pubyear):
    #pubyear = str(pubyear)
    """
    if len(pubyear) == 4:
        messi = pubyear
    else:
    """
    fecha = dt.strptime(pubyear, '%Y-%m-%dT%H:%M:%S.%fZ')
        # messi = ano.strftime("%Y")
    aNio = fecha.year

    #fecha_diccionario = dt.strptime(i["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
    #fecha_diccionario_dt = fecha_diccionario.strftime("%Y")
    return aNio

def addYear(catalog, job):
    try:
        years = catalog['years']
        if (job["published_at"] != ''):
            pubyear = convercioni(job["published_at"])
            pubyear = (str(pubyear))
        else:
            pubyear = "2020"
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = newYear(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year['jobs'], job)
    except Exception:
        return None

def addType(catalog, job):
    try:
        jobs = catalog['info']
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
    sortiao = lt.newList("ARRAY_LIST")
    country = mp.get(data_structs['countries'], cod_pais)
    if country:
        var1 = me.getValue(country)['jobs']
        cant_of_pais = mp.size(var1)
        for i in lt.iterator(var1):
            if xp.lower() == i["experience_level"].lower():
                lt.addLast(lt1, i)
    
    if lt.isEmpty(lt1):
        print("Ningun resultado encontrado")
        sys.exit(0)
    elif lt.size(lt1) >= 2:
        sortiao = merg.sort(lt1, sort_r3)
    elif lt.size(lt1) <= 1:
        sortiao = lt1 

    if n_ofertas > lt.size(sortiao):
        n_ofertas = lt.size(sortiao)
    elif n_ofertas <= lt.size(sortiao):
        n_ofertas = n_ofertas 

    final = lt.subList(sortiao, 1, n_ofertas)
    cant_xp = lt.size(lt1)

    return final, cant_xp, cant_of_pais


def req_2(data_structs, num_ofertas, empresa, ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    filtro = lt.newList('ARRAY_LIST')
    company = mp.get(data_structs["companies"], empresa)

    if company:
        valores = me.getValue(company)["jobs"]
        for job in lt.iterator(valores):
            if ciudad.lower() == job["city"].lower():
                lt.addLast(filtro, job)

    tamanho = lt.size(filtro)

    if lt.isEmpty(filtro):
        print("Ningun resultado encontrado")
        sys.exit(0)
    elif lt.size(filtro) >= 2:
        sortiao = merg.sort(filtro, sort_r3)
    elif lt.size(filtro) <= 1:
        sortiao = filtro 


    if num_ofertas > lt.size(sortiao):
        num_ofertas = lt.size(sortiao)
    elif num_ofertas <= lt.size(sortiao):
        num_ofertas = num_ofertas 
    
    sublista = lt.subList(sortiao, 1, num_ofertas)

    return sublista, tamanho


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
    fecha_inicial_dt = str(dt.strptime(fecha_inicial_consulta, "%Y-%m-%d"))
    fecha_final_dt = str(dt.strptime(fecha_final_consulta, "%Y-%m-%d"))
    chili = lt.newList("ARRAY_LIST")
    lt1 = lt.newList("ARRAY_LIST")
    country = mp.get(data_structs['countries'], cod_pais)
    #print(country)
    if country:
        var1 = me.getValue(country)['jobs']
        for i in lt.iterator(var1):
            fecha_diccionario = dt.strptime(i["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
            fecha_diccionario_dt = fecha_diccionario.strftime("%Y-%m-%d")
            if fecha_inicial_dt <= fecha_diccionario_dt and fecha_diccionario_dt <= fecha_final_dt:
                lt.addLast(chili, i)
    
    if lt.size(chili) >= 2:
        sortiao = merg.sort(chili, sort_r3)
    elif lt.size(chili) <= 1:
        sortiao = chili 

    if lt.isEmpty(chili):
        print("Ningun resultado encontrado")
        sys.exit(0)

    cant_of_pais = lt.size(chili)


    return sortiao, cant_of_pais


def req_5(data_structs, ciudad, fecha_inicial_consulta, fecha_final_consulta):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    fecha_inicial_dt = str(dt.strptime(fecha_inicial_consulta, "%Y-%m-%d"))
    fecha_final_dt = str(dt.strptime(fecha_final_consulta, "%Y-%m-%d"))
    lttot = lt.newList("ARRAY_LIST")
    ltm = lt.newList("ARRAY_LIST")
    ltsr = lt.newList("ARRAY_LIST")
    chili = lt.newList("ARRAY_LIST")
    
    city = mp.get(data_structs['cities'], ciudad)
    #print(city)
    if city:
        var1 = me.getValue(city)['jobs']
        for i in lt.iterator(var1):
            fecha_diccionario = dt.strptime(i["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
            fecha_diccionario_dt = fecha_diccionario.strftime("%Y-%m-%d")
            if fecha_inicial_dt <= fecha_diccionario_dt and fecha_diccionario_dt <= fecha_final_dt:
                lt.addLast(chili, i)
    
    tot_of = lt.size(chili)

    if lt.size(chili) >= 2:
        sortiao = merg.sort(chili, sort_r3)
    elif lt.size(chili) <= 1:
        sortiao = chili 

    if lt.isEmpty(chili):
        print("Ningun resultado encontrado")
        sys.exit(0)

    return sortiao, tot_of


def req_6(data_structs, cant_ciu, xp, ano):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    ano_fi = ano
    info_lt = lt.newList("ARRAY_LIST")
    chili = lt.newList("ARRAY_LIST")
    
    if xp == "indiferente":
        res = mp.get(data_structs['years'], ano_fi)
        if res:
            var1 = me.getValue(res)["jobs"]
            for i in lt.iterator(var1):
                lt.addLast(chili, i)
                ide_info = i["id"]
                info = mp.get(data_structs['info'], ide_info)
                if info:
                    var2 = me.getValue(info)["jobs"]
                    for q in lt.iterator(var2):
                        lt.addLast(info_lt, q)
    elif xp == "junior" or xp == "mid" or xp == "senior":
        res = mp.get(data_structs['xps'], xp)
        if res:
            var1 = me.getValue(res)["jobs"]
            for i in lt.iterator(var1):
                fecha_diccionario = dt.strptime(i["published_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
                fecha_final = fecha_diccionario.strftime("%Y")
                if fecha_final == ano:
                    ide_info = i["id"]
                    lt.addLast(chili, i)
                    info = mp.get(data_structs['info'], ide_info)
                    if info:
                        var2 = me.getValue(info)["jobs"]
                        for q in lt.iterator(var2):
                            lt.addLast(info_lt, q)

    else:
        print("nivel de xp no valido")
        sys.exit(0)

    tot_of = lt.size(chili)

    #datos = req64(data_structs, chili, info_lt)
    datos = req64(chili, info_lt)
    cant_empresas = req62(chili)

    if lt.size(datos) >= 2:
        sortiao = merg.sort(datos, sort_r6)
    elif lt.size(datos) <= 1:
        sortiao = datos 
    if lt.isEmpty(datos):
        print("Ningun resultado encontrado")
        sys.exit(0)

    #print(sortiao)
    finalissima = lt.subList(sortiao, 1, cant_ciu)

    return finalissima, tot_of, sortiao, cant_empresas

def req62(lst):
    cr7 = lt.newList("ARRAY_LIST")

    for i in lt.iterator(lst):
        if lt.isPresent(cr7, i["company_name"]) == 0:
            lt.addLast(cr7, i["company_name"])
        else:
            batman = 0
    
    return cr7



def req64(lst, info_lt):
    fin = {}
    for i in lt.iterator(lst):
        fin[i['id']] = i

    info_ciu = defaultdict(dict)

    for x in lt.iterator(info_lt):
        of = fin[x["id"]]
        ciudad = of["city"]
        pais = of["country_code"]
        empresa = of["company_name"]
        if x["salary_from"] == "" or x["salary_to"] == "":
            sal_min = 0
            sal_max = 0
        else:
            sal_min = int(x["salary_from"])
            sal_max = int(x["salary_to"])

        if "total_ofertas" not in info_ciu[ciudad]:
            info_ciu[ciudad]["total_ofertas"] = 0
            info_ciu[ciudad]["salario"] = []
            info_ciu[ciudad]["cant_empresas"] = defaultdict(int)
            info_ciu[ciudad]["pais"] = pais
        elif info_ciu[ciudad]["pais"] != pais:
            info_ciu[ciudad]["pais"] = pais

        info_ciu[ciudad]["total_ofertas"] += 1
        info_ciu[ciudad]["salario"].extend([sal_min, sal_max])
        info_ciu[ciudad]["cant_empresas"][empresa] += 1

    for q, k in info_ciu.items():
        salarios = k["salario"]
        salario_promedio = sum(salarios) / len(salarios)
        k['salario_promedio'] = salario_promedio

    for q, k in info_ciu.items():
        empresa_mas_ofertas = max(k["cant_empresas"], key=k["cant_empresas"].get)
        cantidad_ofertas_empresa_mas = k["cant_empresas"][empresa_mas_ofertas]
        k['empresa_mas_ofertas'] = empresa_mas_ofertas
        k['cantidad_ofertas_empresa_mas'] = cantidad_ofertas_empresa_mas

    for q, k in info_ciu.items():
        salarios = k["salario"]
        mejor_oferta = max(salarios)
        peor_oferta = min(salarios)
        k['mejor_oferta'] = mejor_oferta
        k['peor_oferta'] = peor_oferta

    finalissima = lt.newList("ARRAY_LIST")
    for ciudad, info in info_ciu.items():
        lt.addLast(finalissima, {'ciudad': ciudad,
                          'pais': info['pais'],
                          'total_ofertas': info['total_ofertas'],
                          'salario_promedio': info['salario_promedio'],
                          "cant_empresas": len(info["cant_empresas"]),
                          'empresa_mas_ofertas': info['empresa_mas_ofertas'],
                          'cantidad_ofertas_empresa_mas': info['cantidad_ofertas_empresa_mas'],
                          'mejor_oferta': info['mejor_oferta'],
                          'peor_oferta': info['peor_oferta']})

    return finalissima


def req_7(data_structs, num_ofertas, anho, mes):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    list_mes = lt.newList("ARRAY_LIST")
    ides = lt.newList("ARRAY_LIST")
    #sacar del mapa years los trabajos que cumplen con el año y el mes
    anio = str(dt.strptime(anho, "%Y"))
    mess = str(dt.strptime(mes, "%m"))


    filt_anho = mp.get(data_structs["years"], anio)

    if filt_anho:
        var1 = me.getValue(filt_anho)["jobs"]

        for i in lt.iterator(var1):
            if i[mess] == mes:
                lt.addLast(list_mes, i) #lista de las ofertas que funcionan

            #obtener el id de cada oferta posible
            ide_info = i["id"]
            info = lt.getElement(list_mes, ide_info)
            lt.addLast(ides, info) #ides de las ofertas que funcionan


    num = 0
    
    for ofertas in range(len(list_mes)):
        todos_paises = {"country": ofertas["country_code"], 
                        "numero_ofertas": num, 
                        "empresa":ofertas["company_name"]}

        if ofertas["country_code"] in todos_paises["country"]:
            num +=1
        else:
            todos_paises["country"] = ofertas["country_code"]
        #retorna un diccionario con la lista de los paises y cuantas ofertas tiene cada uno

    #hacer un sorted 

    if lt.size(list_mes) >= 2:
        sortiao = merg.sort(list_mes, sortr7)
    elif lt.size(list_mes) <= 1:
        sortiao = list_mes
    if lt.isEmpty(list_mes):
        print("Ningun resultado encontrado")
        sys.exit(0)


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

def sort_r6(oferta1, oferta2):
    cant_of1 = int(oferta1['total_ofertas'])
    cant_of2 = int(oferta2['total_ofertas'])
    name1 = oferta1['ciudad']
    name2 = oferta2['ciudad']
    if cant_of1 > cant_of2:
        return True
    elif cant_of1 == cant_of2:
        if name1 < name2:
            return True
        else:
            return False
    else:
        return False

def sortr7(diccionario):
    num_ofertas = diccionario["numero_ofertas"]
    mayor = 0
    
    for i in range(len(diccionario)):
        name1 = i["empresa"]
        name2 = i+1["empresa"]

    if num_ofertas > mayor:
        mayor = num_ofertas
        #mayor_cod = diccionario["country"]
        return True
    elif num_ofertas == mayor:
        if name1 < name2:
            return True
        else:
            return False
    else:
        return False

        

def compareDate():
    pass