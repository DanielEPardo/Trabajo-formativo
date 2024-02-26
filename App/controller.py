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
csv.field_size_limit(2147483647)

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

def load_data(control, suffix):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    catalog = control['model']
    
    jobsSize = loadJobs(catalog, suffix)
    loadTypes(catalog, suffix)
    loadLocations(catalog, suffix)
    loadSkills(catalog, suffix)
    
    return jobsSize

def loadJobs(catalog, suffix):
    filename = cf.data_dir + suffix + "-jobs.csv"
    inputfile = csv.DictReader(open(filename, encoding="utf-8"), delimiter= ";")
    for job in inputfile:
        model.addJobs(catalog, job)
        
    return model.jobsSize(catalog)


def loadTypes(catalog, suffix):
    filename = cf.data_dir + suffix + "-employments_types.csv"
    inputfile = csv.DictReader(open(filename, encoding= "utf-8"), delimiter= ";")
    for type in inputfile:
        model.addTypes(catalog, type)
        

def loadLocations(catalog, suffix):
    filename = cf.data_dir + suffix + "-multilocations.csv"
    inputfile = csv.DictReader(open(filename, encoding= "utf-8"), delimiter= ";")
    for location in inputfile:
        model.addLocations(catalog, location)


def loadSkills(catalog, suffix):
    filename = cf.data_dir + suffix + "-skills.csv"
    inputfile = csv.DictReader(open(filename, encoding= "utf-8"), delimiter= ";")
    for skill in inputfile:
        model.addSkills(catalog, skill)


def getFirstAndLast3Jobs(control):
    """
    Retorna los primeros y los ultimos 3 results
    """
    catalog = control["model"]
    return model.getFirstAndLast3Jobs(catalog)

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, numero, pais, nivel):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    catalog = control["model"]
    start = get_time()
    totalOfertas, listaOfertas = model.req_1(catalog, numero, pais, nivel)
    fin = get_time()
    dif = delta_time(start, fin)
    return totalOfertas, listaOfertas, dif


def req_2(control, nombre, fecha0, fechaf):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    catalog = control['model']
    start = get_time()
    totalOfertas, contjunior, contmid, contsenior, listaOfertas = model.req_2(catalog, nombre, fecha0, fechaf)
    fin = get_time()
    dif = delta_time(start, fin)
    return totalOfertas, contjunior, contmid, contsenior, listaOfertas, dif


def req_3(control, numberOfOffersToShow, company, city):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    catalog = control["model"]
    start = get_time()
    totalOfertas, listaOfertas = model.req_3(catalog, numberOfOffersToShow, company, city)
    end = get_time()
    diff = delta_time(start, end)
    return totalOfertas, listaOfertas, diff


def req_4(control, country, fechaInicio, fechaFinal):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    catalog = control['model']
    start = get_time()
    totalOfertas, totalEmpresas, totalCiudades, ciudadMayor, ciudadMenor, listaOfertas = model.req_4(catalog, country, fechaInicio, fechaFinal)
    end = get_time()
    diff = delta_time(start, end)
    return totalOfertas, totalEmpresas, totalCiudades, ciudadMayor, ciudadMenor, listaOfertas, diff


def req_5(control, city, fechaInicio, fechaFinal):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    catalog = control["model"]
    start = get_time()
    totalOfertas, totalEmpresas, empresaMayor, empresaMenor, listaOfertas = model.req_5(catalog, city, fechaInicio, fechaFinal)
    end = get_time()
    diff = delta_time(start, end)
    return totalOfertas, totalEmpresas, empresaMayor, empresaMenor, listaOfertas, diff
    

def req_6(control, numberOfOffersToShow, experienceLevel, country, startDate, endDate):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    catalog = control['model']
    start = get_time()
    totalCiudades, totalEmpresas, totalOfertas, promSalario, ciudadMayor, ciudadMenor, listaOfertas = model.req_6(catalog, numberOfOffersToShow, experienceLevel, country, startDate, endDate)
    end = get_time()
    diff = delta_time(start, end)
    return totalCiudades, totalEmpresas, totalOfertas, promSalario, ciudadMayor, ciudadMenor, listaOfertas, diff


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