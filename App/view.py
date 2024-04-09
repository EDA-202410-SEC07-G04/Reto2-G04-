"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from collections import Counter
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
#from tabulate import tabulate
assert cf
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000

sys.setrecursionlimit(default_limit*10)


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")

def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer:.3f}")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    respuesta = controller.load_data(control)
    print(" Termino load data ")
    size = mp.size(control["model"]["jobs"])
    print(size)
    messi = mp.size(control["model"]["years"])
    print(messi)
    #print(control["model"]["companies"])

    """
    lista = controller.get_jobs_sublist(control)
    print(lista)
    print(tabulate(list(lt.iterator(lista[0]))+list(lt.iterator(lista[1])), headers="keys", tablefmt="grid"))
    """

    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    n_ofertas = int(input("Digame la cantidad de ofertas que desea ver: "))
    cod_pais = str(input("Digame el pais del cual desea consultar ofertas: "))
    xp = str(input("Digame el nivel de experiencia que le interesa: "))
    final, cant_xp, cant_of_pais, deltaTime = controller.req_1(control, n_ofertas, cod_pais.lower(), xp)
    print("            ")
    print("El total de ofertas en ese pais: " + str(cant_of_pais))
    print("El total de ofertas por el nivel de experiencia en ese pais: " + str(cant_xp))
    size = lt.size(final)    
    sample = size
    if size == 1:
        job = lt.getElement(final, 0)
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    elif size <= sample*2:
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        for job in lt.iterator(final):
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    else:
        print("Los", sample, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        i = 1
        while i <= sample:
            job = lt.getElement(final, i)
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
            i += 1
    DeltaTime = f"{deltaTime:.3f}"
    print("Para este req el tiempo es:", str(DeltaTime), "[ms]")

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    num_ofertas = int(input("Cantidad de ofertas que desea ver: "))
    empresa = str(input("Empresa de la cual desea consultar las ofertas: "))
    ciudad = str(input("Ciudad de la cual desea ver las ofertas: "))

    sublista, tamanho, deltaTime = controller.req_2(control, num_ofertas, empresa.lower(), ciudad.lower())
    size = tamanho
    print("            ")
    print("El total de ofertas en esta empresa y ciudad es : " + str(tamanho))
    sample = size
    if size == 1:
        job = lt.getElement(sublista, 0)
        print("Los", num_ofertas, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    elif size <= sample*2:
        print("Los", num_ofertas, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        for job in lt.iterator(sublista):
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    else:
        print("Los", num_ofertas, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        i = 1
        while i <= sample:
            job = lt.getElement(sublista, i)
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
            i += 1
    DeltaTime = f"{deltaTime:.3f}"
    print("Para este req el tiempo es:", str(DeltaTime), "[ms]")


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    nom_empresa = str(input("Digame el nombre de la empresa: "))
    fecha_inicial_consulta =  str(input("Que fecha minima le interesa?: "))
    fecha_final_consulta = str(input("Que fecha maxima le interesa?: "))

    sortiao, cant_of, cant_xp_jr, cant_xp_m, cant_xp_sr, deltaTime  = controller.req_3(control, nom_empresa.lower(), fecha_inicial_consulta, fecha_final_consulta)
    print("            ")
    print("Numero total de ofertas: " + str(cant_of))
    print("Numero de ofertas con xp Junior: " + str(cant_xp_jr))
    print("Numero de ofertas con xp Mid: " + str(cant_xp_m))
    print("Numero de ofertas con xp Senior: " + str(cant_xp_sr))
    size = lt.size(sortiao)    
    sample = size
    if size == 1:
        job = lt.getElement(sortiao, 0)
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    elif size <= sample*2:
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        for job in lt.iterator(sortiao):
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    else:
        print("Los", sample, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        i = 1
        while i <= sample:
            job = lt.getElement(sortiao, i)
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
            ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
            job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
            ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
            i += 1
    DeltaTime = f"{deltaTime:.3f}"
    print("Para este req el tiempo es:", str(DeltaTime), "[ms]")

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    cant_empresas_una_oferta = []
    ciudades = []
    messi = lt.newList("ARRAY_LIST")
    cr7 = lt.newList("ARRAY_LIST")
    mes = 0
    cod_pais = str(input("Digame el pais del cual desea consultar ofertas: "))
    fecha_inicial_consulta =  str(input("Que fecha minima le interesa?: "))
    fecha_final_consulta = str(input("Que fecha maxima le interesa?: "))
    

    final, cantidad, deltaTime = controller.req_4(control, cod_pais.lower(), fecha_inicial_consulta, fecha_final_consulta)
    for i in lt.iterator(final):
        ciudades.append(i["city"])
        if lt.isPresent(messi, i["company_name"]) == 0:
            lt.addLast(messi, i["company_name"])
        else:
            mes += 1

    tot_emp = lt.size(messi)

    contador = Counter(ciudades)
    elemento_mayor, frecuencia_mayor = contador.most_common(1)[0]    
    elemento_menor, frecuencia_menor = contador.most_common()[-1]

    print("            ")
    print("Numero total de ofertas: " + str(cantidad))
    print("Numero de empresas que publicaron al menos una oferta: " + str(tot_emp))
    print("Ciudad con mayor número de ofertas: " + str(elemento_mayor) + " número de empleos " + str(frecuencia_mayor))
    print("Ciudad con menor número de ofertas: " + str(elemento_menor) + " número de empleos " + str(frecuencia_menor))

    size = lt.size(final)    
    sample = size
    if size == 1:
        job = lt.getElement(final, 0)
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] + ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + 
        ' Ciudad: ' + job['city'] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + ' Remoto?: ' + job['remote_interview'] + 
        ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    elif size <= sample*2:
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        for job in lt.iterator(final):
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] + ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + 
        ' Ciudad: ' + job['city'] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + ' Remoto?: ' + job['remote_interview'] + 
        ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    else:
        print("Los", sample, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        i = 1
        while i <= sample:
            job = lt.getElement(final, i)
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] + ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + 
        ' Ciudad: ' + job['city'] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + ' Remoto?: ' + job['remote_interview'] + 
        ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
            i += 1
    DeltaTime = f"{deltaTime:.3f}"
    print("Para este req el tiempo es:", str(DeltaTime), "[ms]")

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    cant_empresas_una_oferta = []
    empresas = []
    messi = lt.newList("ARRAY_LIST")
    mes = 0
    nom_ciudad = str(input("Digame el nombre de la ciudad: "))
    fecha_inicial_consulta =  str(input("Que fecha minima le interesa?: "))
    fecha_final_consulta = str(input("Que fecha maxima le interesa?: "))

    final, cantidad, deltaTime = controller.req_5(control, nom_ciudad.lower(), fecha_inicial_consulta, fecha_final_consulta)
    for i in lt.iterator(final):
        empresas.append(i["company_name"])
        if lt.isPresent(messi, i["company_name"]) == 0:
            lt.addLast(messi, i["company_name"])
        else:
            mes += 1

    tot_emp = lt.size(messi)

    contador = Counter(empresas)
    elemento_mayor, frecuencia_mayor = contador.most_common(1)[0]    
    elemento_menor, frecuencia_menor = contador.most_common()[-1]

    print("            ")
    print("Numero total de ofertas: " + str(cantidad))
    print("Numero de empresas que publicaron al menos una oferta: " + str(tot_emp))
    print("Empresa con mayor número de ofertas: " + str(elemento_mayor) + " número de empleos " + str(frecuencia_mayor))
    print("Empresa con menor número de ofertas: " + str(elemento_menor) + " número de empleos " + str(frecuencia_menor))
    size = lt.size(final)    
    sample = size
    if size == 1:
        job = lt.getElement(final, 0)
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  ' Nombre de la compañia: ' + job['company_name'] +
            " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'])
    elif size <= sample*2:
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        for job in lt.iterator(final):
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  ' Nombre de la compañia: ' + job['company_name'] +
            " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'])
    else:
        print("Los", sample, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        i = 1
        while i <= sample:
            job = lt.getElement(final, i)
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  ' Nombre de la compañia: ' + job['company_name'] +
            " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'])
            i += 1
    DeltaTime = f"{deltaTime:.3f}"
    print("Para este req el tiempo es:", str(DeltaTime), "[ms]")

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    cant_ciu = int(input("Digame la cantidad de ciudades que desea consultar: "))
    xp = str(input("Digame el nivel de experiencia que le interesa (en caso de no estar interesado en uno en especifico escriba indiferente): "))
    ano = str(input("Digame el año que le interesa(XXXX): "))

    final, cantc, messi, cant_empresas = controller.req_6(control, cant_ciu, xp.lower(), ano)

    ciu_may = lt.getElement(final, 1)
    #print(ciu_may)
    ciu_men = lt.getElement(messi, 0)
    #print(ciu_men)

    print("            ")
    print("Ciudades que cumplen con las condiciones: " + str(lt.size(final)))
    print("Total de empresas que cumplen con las condiciones: " + str(lt.size(cant_empresas)))
    print("Numero total de ofertas que cumplen con las condiciones: " + str(cantc))
    print("Ciudad con mayor número de ofertas: " + str(ciu_may["ciudad"]) + " número de empleos: " + str(ciu_may["total_ofertas"]))
    print("Ciudad con menor número de ofertas: " + str(ciu_men["ciudad"]) + " número de empleos: " + str(ciu_men["total_ofertas"]))
    size = lt.size(final)    
    sample = size
    if size == 1:
        job = lt.getElement(final, 0)
        print("Las", size, "ciudades ordenadas por cantidad de ofertas son: ")
        print("            ")
        print('ciudad: ' + job["ciudad"] + ' Pais: ' + job['pais'] +  ' Ofertas en la ciudad: ' + str(job['total_ofertas']) +
            " salario promedio: " + str(job["salario_promedio"]) + ' empresas con al menos una oferta: ' + str(job['cant_empresas']) + 
            ' empresa con mas ofertas en esa ciudad: ' + job['empresa_mas_ofertas'] + ' conteo: ' + str(job['cantidad_ofertas_empresa_mas']) + 
            ' mejor oferta en la ciudad: ' + str(job['mejor_oferta']) + ' peor oferta en la ciudad: ' + str(job['peor_oferta']))
    elif size <= sample*2:
        print("Las", size, "ciudades ordenadas por cantidad de ofertas son: ")
        for job in lt.iterator(final):
            print("            ")
            print('ciudad: ' + job["ciudad"] + ' Pais: ' + job['pais'] +  ' Ofertas en la ciudad: ' + str(job['total_ofertas']) +
            " salario promedio: " + str(job["salario_promedio"]) + ' empresas con al menos una oferta: ' + str(job['cant_empresas']) + 
            ' empresa con mas ofertas en esa ciudad: ' + job['empresa_mas_ofertas'] + ' conteo: ' + str(job['cantidad_ofertas_empresa_mas']) + 
            ' mejor oferta en la ciudad: ' + str(job['mejor_oferta']) + ' peor oferta en la ciudad: ' + str(job['peor_oferta']))
    else:
        print("Las", sample, "ciudades ordenadas por cantidad de ofertas son: ")
        i = 1
        while i <= sample:
            job = lt.getElement(final, i)
            print("            ")
            print('ciudad: ' + job["ciudad"] + ' Pais: ' + job['pais'] +  ' Ofertas en la ciudad: ' + str(job['total_ofertas']) +
            " salario promedio: " + str(job["salario_promedio"]) + ' empresas con al menos una oferta: ' + str(job['cant_empresas']) + 
            ' empresa con mas ofertas en esa ciudad: ' + job['empresa_mas_ofertas'] + ' conteo: ' + str(job['cantidad_ofertas_empresa_mas']) + 
            ' mejor oferta en la ciudad: ' + str(job['mejor_oferta']) + ' peor oferta en la ciudad: ' + str(job['peor_oferta']))
            i += 1
    


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    default_limit = 1000
    sys.setrecursionlimit(default_limit*10)
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            #mem = True
            print("Cargando información de los archivos ....\n")
            load_data(control)
            #answer = controller.load_data(control)
            #printLoadDataAnswer(answer)

        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
