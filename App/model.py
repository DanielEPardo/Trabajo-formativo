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
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import datetime
from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {"types": None,
                    "jobs": None,
                    "locations": None,
                    "skills": None}
    
    data_structs["types"] = lt.newList("ARRAY_LIST")
    data_structs["jobs"] = lt.newList("ARRAY_LIST")
    data_structs["locations"] = lt.newList("ARRAY_LIST")
    data_structs["skills"] = lt.newList("ARRAY_LIST")
    
    return data_structs


# Funciones para agregar informacion al modelo

def addJobs(catalog, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    job['published_at'] = datetime.strptime(job["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
    lt.addLast(catalog['jobs'], job)
    return catalog


def addTypes(catalog, type):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(catalog['types'], type)
    return catalog


def addLocations(catalog, location):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(catalog['locations'], location)
    return catalog


def addSkills(catalog, skill):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(catalog['skills'], skill)
    return catalog


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def getFirstAndLast3Jobs(catalog):
    """
    Retorna los primeros y los ultimos 3 jobs
    """
    jobsCatalog = catalog["jobs"]
    sa.sort(jobsCatalog, sortByDateCriteria)

    firstAndLast3JobsList = lt.newList("ARRAY_LIST")
    first3 = lt.subList(jobsCatalog, 1, 3)
    last3 = lt.subList(jobsCatalog, lt.size(jobsCatalog) - 2, 3)
    
    for item in lt.iterator(first3):
        newItem = {"published_at": item["published_at"].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                   "title": item["title"],
                   "company_name": item["company_name"],
                   "experience_level": item["experience_level"],
                   "country_code": item["country_code"],
                   "city": item["city"]}
        lt.addLast(firstAndLast3JobsList, newItem)
        
    for item in lt.iterator(last3):
        newItem = {"published_at": item["published_at"].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                   "title": item["title"],
                   "company_name": item["company_name"],
                   "experience_level": item["experience_level"],
                   "country_code": item["country_code"],
                   "city": item["city"]}
        lt.addLast(firstAndLast3JobsList, newItem)
    
    return firstAndLast3JobsList


def getFirstAndLast3(data):
    """
    Retorna los primeros y los ultimos 3 datos
    """
    dataCatalog = data

    firstAndLast3DataList = lt.newList("ARRAY_LIST")
    first3 = lt.subList(dataCatalog, 1, 3)
    last3 = lt.subList(dataCatalog, lt.size(dataCatalog) - 2, 3)

    for firstItem in lt.iterator(first3):
        lt.addLast(firstAndLast3DataList, firstItem)

    for lastItem in lt.iterator(last3):
        lt.addLast(firstAndLast3DataList, lastItem)

    return firstAndLast3DataList


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def jobsSize(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["jobs"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(catalog, numberOfOffersToShow, company, city):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    jobsList = catalog['jobs']
    
    filteredList = lt.newList("ARRAY_LIST")
    for offer in lt.iterator(jobsList):
        if offer['company_name'] == company and offer['city'] == city:
            item = {'published_at': offer['published_at'].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'country_code': offer['country_code'],
                    'city': offer['city'],
                    'company_name': offer['company_name'],
                    'title': offer['title'],
                    'experience_level': offer['experience_level'],
                    'remote_interview': offer['remote_interview'],
                    'workplace_type': offer['workplace_type']}
            lt.addLast(filteredList, item)
    
    orderedList = sa.sort(filteredList, sortByDateCriteria)
    totalOfertas = lt.size(orderedList)
    
    if totalOfertas < numberOfOffersToShow:
        listaOfertas = orderedList
    else:
        listaOfertas = lt.subList(orderedList, 1, numberOfOffersToShow)
        
    if lt.size(listaOfertas) > 6:
        listaOfertas = getFirstAndLast3(listaOfertas)
    
    return totalOfertas, listaOfertas
                


def req_4(catalog, country, fechaInicio, fechaFinal):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    jobsList = catalog['jobs']
    
    companies_list = lt.newList("ARRAY_LIST")
    cities_list = lt.newList("ARRAY_LIST")
    cities_dict = {}
    filteredList = lt.newList("ARRAY_LIST")
    for offer in lt.iterator(jobsList):
        date = offer['published_at'].strftime("%Y-%m-%d")
        if offer['country_code'] == country and datetime.strptime(date, '%Y-%m-%d') >= datetime.strptime(fechaInicio, '%Y-%m-%d') and datetime.strptime(date, '%Y-%m-%d') <= datetime.strptime(fechaFinal, '%Y-%m-%d'):
            item = {'published_at': offer['published_at'].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'title': offer['title'],
                    'experience_level': offer['experience_level'],
                    'company_name': offer['company_name'],
                    'city': offer['city'],
                    'workplace_type': offer['workplace_type'],
                    'remote_work' : 'True' if offer['workplace_type'] == "remote" else 'False', 
                    'open_to_hire_ukrainians': offer['open_to_hire_ukrainians']}
            lt.addLast(filteredList, item)
            if lt.isPresent(companies_list, offer['company_name']) == 0:
                lt.addLast(companies_list, offer['company_name'])
            pos_city = lt.isPresent(cities_list, offer['city'])
            if pos_city == 0:
                lt.addLast(cities_list, offer['city'])
                cities_dict[offer['city']] = 1
            else:
                cities_dict[offer['city']] += 1
    
    maxCity = ""
    max = 0
    minCity = ""
    min = 10000000
    for city in cities_dict:
        if cities_dict[city] > max:
            maxCity = city
            max = cities_dict[city]
        if cities_dict[city] < min:
            minCity = city
            min = cities_dict[city]
    
    totalOfertas = lt.size(filteredList)        
    if totalOfertas > 6:
        listaOfertas = getFirstAndLast3(filteredList)
    else:
        listaOfertas = filteredList
        
    return totalOfertas, lt.size(companies_list), lt.size(cities_list), {maxCity: max}, {minCity: min}, listaOfertas
                

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


def sortByDateCriteria(data1, data2):
    return data1["published_at"] > data2["published_at"]


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass