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
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = getTime()
    tracemalloc.start()
    start_memory = getMemory()

    load_jobs(control)
    load_info(control)

    stop_time = getTime()
    delta_time = deltaTime(stop_time, start_time)
    
    stop_memory = getMemory()
    tracemalloc.stop()
    delta_memory = deltaMemory(stop_memory, start_memory)
    return delta_time, delta_memory


    #load_jobs2(control)
    

def subi(control):
    sub1, sub2 = model.get_subi(control["model"])
    return sub1, sub2
# Funciones de ordenamiento

def load_jobs(control):
    #"80-por-jobs.csv"
    #'large-jobs.csv'
    jobsfile = cf.data_dir + 'large-jobs.csv'
    input_file = csv.DictReader(open(jobsfile, encoding='utf-8'), delimiter=';')
    for job in input_file:
        model.addJob(control['model'], job)
        model.addCountrycode(control['model'], job)
        model.addCompanyname(control['model'], job)
        model.addCityname(control['model'], job)
        model.addXpname(control['model'], job)
        model.addYear(control['model'], job)

def load_info(control):
    #'large-employments_types.csv'
    # "10-por-employments_types.csv"
    jobsfile = cf.data_dir + 'large-employments_types.csv'
    input_file = csv.DictReader(open(jobsfile, encoding='utf-8'), delimiter=';')
    for info in input_file:
        model.addType(control['model'], info)
        
    #return model.jobSize(control), model.jobComplete(control)

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass

def get_jobs_sublist (control):
    sublist1, sublist2 = model.get_jobs_sublist(control["model"])
    return sublist1, sublist2

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, n_ofertas, cod_pais, xp):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    final, cant_xp, cant_of_pais = model.req_1(control["model"], n_ofertas, cod_pais, xp)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    return final, cant_xp, cant_of_pais, deltaTime


def req_2(control, num_ofertas, empresa, ciudad):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    sublista, tamanho = model.req_2(control["model"],num_ofertas, empresa, ciudad)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    return sublista, tamanho, deltaTime


def req_3(control, nom_empresa, fecha_inicial_consulta, fecha_final_consulta):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    sortiao, cant_of, cant_xp_jr, cant_xp_m, cant_xp_sr = model.req_3(control["model"], nom_empresa, fecha_inicial_consulta, fecha_final_consulta)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    return sortiao, cant_of, cant_xp_jr, cant_xp_m, cant_xp_sr, deltaTime 


def req_4(control, cod_pais, fecha_inicial_consulta, fecha_final_consulta):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    final, cant = model.req_4(control["model"], cod_pais, fecha_inicial_consulta, fecha_final_consulta)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    return final, cant, deltaTime


def req_5(control, ciudad, fecha_inicial_consulta, fecha_final_consulta):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    final, cantidad = model.req_5(control["model"], ciudad, fecha_inicial_consulta, fecha_final_consulta)
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    return final, cantidad, deltaTime

def req_6(control, cant_ciu, xp, ano):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    final, cantc, messi, cant_empresas = model.req_6(control["model"], cant_ciu, xp, ano) 
    end_time = get_time()
    deltaTime = delta_time(start_time, end_time)
    return final, cantc, messi, cant_empresas, deltaTime


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

csv.field_size_limit(2147483647)