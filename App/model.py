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
from tabulate import tabulate

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


def req_1(catalog, numero, pais, nivel):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    jobsList = catalog['jobs']
    
    listaf = lt.newList("ARRAY_LIST")
    for offer in lt.iterator(jobsList):
        if offer['experience_level'] == nivel and offer['country_code'] == pais:
            item = {'published_at': offer['published_at'].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'title': offer['title'],
                    'company_name': offer['company_name'],
                    'experience_level': offer['experience_level'],
                    'country_code': offer['country_code'],
                    'city': offer['city'],
                    'company_size': offer['company_size'],
                    'workplace_type': offer['workplace_type'],
                    'open_to_hire_ukrainians': offer['open_to_hire_ukrainians']}
            lt.addLast(listaf, item)
    
    listao = sa.sort(listaf, sortByDateCriteria)
    totalOfertas = lt.size(listao)
    
    if totalOfertas < numero:
        listaOfertas = listao
    else:
        listaOfertas = lt.subList(listao, 1, numero)
        
    if lt.size(listaOfertas) > 6:
        listaOfertas = getFirstAndLast3(listaOfertas)
    
    return totalOfertas, listaOfertas

def req_2(catalog, nombre, fecha0, fechaf):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    jobsList = catalog['jobs']
    contjunior = 0
    contmid = 0
    contsenior = 0
    listaF = lt.newList("ARRAY_LIST")
    for offer in lt.iterator(jobsList):
        date = offer['published_at'].strftime("%Y-%m-%d")
        if offer['company_name'] == nombre and datetime.strptime(date, '%Y-%m-%d') >= datetime.strptime(fecha0, '%Y-%m-%d') and datetime.strptime(date, '%Y-%m-%d') <= datetime.strptime(fechaf, '%Y-%m-%d'):
            item = {'published_at': offer['published_at'].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'title': offer['title'],
                    'experience_level': offer['experience_level'],
                    'city': offer['city'],
                    'country_code': offer['country_code'],
                    'company_size': offer['company_size'],
                    'workplace_type': offer['workplace_type'],
                    'open_to_hire_ukrainians': offer['open_to_hire_ukrainians']}
            lt.addLast(listaF, item)
            if offer['experience_level'] == "junior":
                contjunior += 1
            if offer['experience_level'] == "mid":
                contmid += 1
            if offer['experience_level'] == "senior":
                contsenior += 1
            
    listaO = sa.sort(listaF, sortByDateAndCountryCriteria)
    totalOfertas = lt.size(listaO)        
    if totalOfertas > 6:
        listaOfertas = getFirstAndLast3(listaO)
    else:
        listaOfertas = listaO
        
    return totalOfertas, contjunior, contmid, contsenior, listaOfertas


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
            
    orderedList = sa.sort(filteredList, sortByDateAndComapnyCriteria)
    totalOfertas = lt.size(orderedList)        
    if totalOfertas > 6:
        listaOfertas = getFirstAndLast3(orderedList)
    else:
        listaOfertas = orderedList
        
    return totalOfertas, lt.size(companies_list), lt.size(cities_list), {maxCity: max}, {minCity: min}, listaOfertas
                

def req_5(catalog, city, fechaInicio, fechaFinal):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    jobsList = catalog['jobs']
    
    companies_list = lt.newList("ARRAY_LIST")
    companies_dict = {}
    filteredList = lt.newList("ARRAY_LIST")
    for offer in lt.iterator(jobsList):
        date = offer['published_at'].strftime("%Y-%m-%d")
        if offer['city'] == city and datetime.strptime(date, '%Y-%m-%d') >= datetime.strptime(fechaInicio, '%Y-%m-%d') and datetime.strptime(date, '%Y-%m-%d') <= datetime.strptime(fechaFinal, '%Y-%m-%d'):
            item = {'published_at': offer['published_at'].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'title': offer['title'],
                    'experience_level': offer['experience_level'],
                    'company_name': offer['company_name'],
                    'workplace_type': offer['workplace_type'],
                    'company_size': offer['company_size']}
            lt.addLast(filteredList, item)
            pos_company = lt.isPresent(companies_list, offer['company_name'])
            if  pos_company == 0:
                lt.addLast(companies_list, offer['company_name'])
                companies_dict[offer['company_name']] = 1
            else:
                companies_dict[offer['company_name']] += 1
    
    maxCompany = ""
    max = 0
    minCompany = ""
    min = 10000000
    for company in companies_dict:
        if companies_dict[company] > max:
            maxCompany = company
            max = companies_dict[company]
        if companies_dict [company] < min:
            minCompany = company
            min = companies_dict[company]
            
    orderedList = sa.sort(filteredList, sortByDateAndComapnyCriteria)
    totalOfertas = lt.size(orderedList)        
    if totalOfertas > 6:
        listaOfertas = getFirstAndLast3(orderedList)
    else:
        listaOfertas = orderedList
        
    return totalOfertas, lt.size(companies_list), {maxCompany: max}, {minCompany: min}, listaOfertas


def req_6(catalog, numberOfOffersToShow, experienceLevel, country, startDate, endDate):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    jobsList = catalog['jobs']
    typesList = catalog['types']
    
    citiesDict = {}
    filteredList = lt.newList("ARRAY_LIST")
    if country == None:
        promSalario = 'N/A'
        for offer in lt.iterator(jobsList):
            date = offer['published_at'].strftime("%Y-%m-%d")
            if offer['experience_level'] == experienceLevel and datetime.strptime(date, '%Y-%m-%d') >= datetime.strptime(startDate, '%Y-%m-%d') and datetime.strptime(date, '%Y-%m-%d') <= datetime.strptime(endDate, '%Y-%m-%d'):
                item = {'city': offer['city'],
                        'company_name': offer['company_name'],
                        'id': offer['id'],
                        'info': {'published_at': offer['published_at'].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                 'title': offer['title'], 
                                 'country_code': offer['country_code'], 
                                 'workplace_type': offer['workplace_type'], 
                                 'salary_from': None,
                                 'salary_to': None}}
                lt.addLast(filteredList, item)
                if offer['city'] not in citiesDict:
                    citiesDict[offer['city']] = 1
                else:
                    citiesDict[offer['city']] += 1
    else:
        promSalario = 0
        for offer in lt.iterator(jobsList):
            date = offer['published_at'].strftime("%Y-%m-%d")
            if offer['country_code'] == country and offer['experience_level'] == experienceLevel and datetime.strptime(date, '%Y-%m-%d') >= datetime.strptime(startDate, '%Y-%m-%d') and datetime.strptime(date, '%Y-%m-%d') <= datetime.strptime(endDate, '%Y-%m-%d'):
                item = {'city': offer['city'],
                        'company_name': offer['company_name'],
                        'id': offer['id'],
                        'info': {'published_at': offer['published_at'].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                 'title': offer['title'], 
                                 'country_code': offer['country_code'], 
                                 'workplace_type': offer['workplace_type'], 
                                 'salary_from': None,
                                 'salary_to': None}}
                lt.addLast(filteredList, item)
                if offer['city'] not in citiesDict:
                    citiesDict[offer['city']] = 1
                else:
                    citiesDict[offer['city']] += 1
                
    orderedByIdJobsList = sa.sort(filteredList, sortByIdCriteria)
    
    afterTypesFilteredList = lt.newList('ARRAY_LIST')
    if isinstance(promSalario, int):
        acumSalario = 0
        cont = 0
    for type in lt.iterator(typesList):
        job_pos = binary_search(orderedByIdJobsList, 1, lt.size(orderedByIdJobsList), type['id'])
        if job_pos != -1:
            job = lt.getElement(orderedByIdJobsList, job_pos)
            salaryInf = int(type['salary_from']) if type['salary_from'] != "" else 0
            salarySup = int(type['salary_to']) if type['salary_to'] != "" else 0
            item = {'city': job['city'],
                    'company_name': job['company_name'],
                    'info': {'published_at': job['info']['published_at'],
                             'title': job['info']['title'], 
                             'country_code': job['info']['country_code'],
                             'workplace_type': job['info']['workplace_type'], 
                             'salary_from': salaryInf,
                             'salary_to': salarySup}}
            lt.addLast(afterTypesFilteredList, item)
            if isinstance(promSalario, int):
                if salaryInf != 0 and salarySup != 0:    
                    acumSalario += (salaryInf + salarySup) / 2
                    cont += 1
    if isinstance(promSalario, int):
        promSalario = round(acumSalario / cont, 2)  
    
    maxCityOverall = ''
    maxOverall = 0
    minCityOverall = ''
    minOverall = 10000000
    for city in citiesDict:
        if citiesDict[city] > maxOverall:
            maxCityOverall = city
            maxOverall = citiesDict[city]
        if citiesDict[city] < minOverall:
            minCityOverall = city
            minOverall = citiesDict[city]
    
    citiesList = lt.newList("ARRAY_LIST")
    companiesList = lt.newList("ARRAY_LIST")
    groupedByCityList = lt.newList("ARRAY_LIST")
    for newOffer in lt.iterator(afterTypesFilteredList):
        if lt.isPresent(companiesList, newOffer['company_name']) == 0:
            lt.addLast(companiesList, newOffer['company_name'])
        pos_city = lt.isPresent(citiesList, newOffer['city'])
        if pos_city == 0:
            lt.addLast(citiesList, newOffer['city'])
            newItem = {'city': newOffer['city'],
                       'cant_offers': 1,
                       'salary_acum': ((newOffer['info']['salary_from'] + newOffer['info']['salary_to']) / 2),
                       'companies': {newOffer['company_name']: 1},
                       'best_offer': newOffer['info'],
                       'worst_offer': newOffer['info']}
            lt.addLast(groupedByCityList, newItem)
        else:
            itemToUpdate = lt.getElement(groupedByCityList, pos_city)
            itemToUpdate['cant_offers'] += 1
            itemToUpdate['salary_acum'] += ((newOffer['info']['salary_from'] + newOffer['info']['salary_to']) / 2)
            dictCompanies = itemToUpdate['companies']
            if newOffer['company_name'] in dictCompanies:
                dictCompanies[newOffer['company_name']] += 1
            else:
                dictCompanies[newOffer['company_name']] = 1
                
            if newOffer['info']['salary_to'] != 0 and newOffer['info']['salary_to'] > itemToUpdate['best_offer']['salary_to']:
                itemToUpdate['best_offer'] = newOffer['info']
            if newOffer['info']['salary_to'] != 0 and newOffer['info']['salary_to'] < itemToUpdate['worst_offer']['salary_to']:
                itemToUpdate['worst_offer'] = newOffer['info']
            lt.changeInfo(groupedByCityList, pos_city, itemToUpdate)
    
    unorderedList = lt.newList('ARRAY_LIST')         
    for city in lt.iterator(groupedByCityList):
        maxCompany = ""
        max = 0
        for company in city['companies']:
            if city['companies'][company] > max:
                maxCompany = company
                max = city['companies'][company]
        bestOffer = lt.newList('ARRAY_LIST')
        lt.addLast(bestOffer, city['best_offer'])
        worstOffer = lt.newList('ARRAY_LIST')
        lt.addLast(worstOffer, city['worst_offer'])
        item = {'city': city['city'],
                'cant_offers': city['cant_offers'],
                'prom_salaries': city['salary_acum'] / city['cant_offers'],
                'cant_empresas': len(city['companies']),
                'max_company': {maxCompany: max},
                'best_offer': tabulate(lt.iterator(bestOffer), tablefmt= 'grid', headers= 'keys', maxcolwidths= 6),
                'worst_offer': tabulate(lt.iterator(worstOffer), tablefmt= 'grid', headers= 'keys', maxcolwidths= 6)}
        lt.addLast(unorderedList, item)
    
    orderedList = sa.sort(unorderedList, sortByCantAndSalaryAndCityCriteria)
    
    if lt.size(orderedList) > numberOfOffersToShow:
        offersList = lt.subList(orderedList, 1, numberOfOffersToShow)
    else:
        offersList = orderedList
        
    totalOfertas = lt.size(offersList)        
    if totalOfertas > 6:
        listaOfertas = getFirstAndLast3(offersList)
    else:
        listaOfertas = offersList
        
    return lt.size(citiesList), lt.size(companiesList), lt.size(filteredList), promSalario, {maxCityOverall: maxOverall}, {minCityOverall: minOverall}, listaOfertas        
        
        
def req_7(catalog, numberOfOffersToShow, fechaInicio, fechaFinal):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    jobsList = catalog['jobs']
    skillsList = catalog['skills']
    
    countriesDict = {}
    citiesDict = {}
    citiesList = lt.newList('ARRAY_LIST')
    filteredList = lt.newList('ARRAY_LIST')
    for offer in lt.iterator(jobsList):
        date = offer['published_at'].strftime("%Y-%m-%d")
        if datetime.strptime(date, '%Y-%m-%d') >= datetime.strptime(fechaInicio, '%Y-%m-%d') and datetime.strptime(date, '%Y-%m-%d') <= datetime.strptime(fechaFinal, '%Y-%m-%d'):
            item = {'id': offer['id'],
                    'experience_level': offer['experience_level'],
                    'country_code': offer['country_code'],
                    'skills': lt.newList('ARRAY_LIST'),
                    'company_name': offer['company_name'],
                    'acum_level': 0,
                    'cont_level': 0,
                    'city': offer['city']}
            lt.addLast(filteredList, item)
            
            if lt.isPresent(citiesList, offer['city']) == 0:
                lt.addLast(citiesList, offer['city'])
                
            if offer['country_code'] not in countriesDict:
                countriesDict[offer['country_code']] = 1
            else:
                countriesDict[offer['country_code']] += 1
                
            if offer['city'] not in citiesDict:
                citiesDict[offer['city']] = 1
            else:
                citiesDict[offer['city']] += 1
                
    maxCountry = ''
    maxCo = 0
    for country in countriesDict:
        if countriesDict[country] > maxCo:
            maxCountry = country
            maxCo =countriesDict[country]
            
    maxCity = ''
    maxC = 0
    for city in citiesDict:
        if citiesDict[city] > maxC:
            maxCity = city
            maxC =citiesDict[city]
    
    orderedByIdJobsList = sa.sort(filteredList, sortByIdCriteria)
    
    afterSkillsFilteredList = lt.newList('ARRAY_LIST')
    idList = lt.newList('ARRAY_LIST')
    for skill in lt.iterator(skillsList):
        job_pos = binary_search(orderedByIdJobsList, 1, lt.size(orderedByIdJobsList), skill['id'])
        if job_pos != -1:
            job = lt.getElement(orderedByIdJobsList, job_pos)
            lt.addLast(job['skills'], skill['name'])
            job['acum_level'] += int(skill['level'])
            job['cont_level'] += 1
            id_pos = lt.isPresent(idList, job['id'])
            if id_pos == 0:
                lt.addLast(idList, job['id'])
                lt.addLast(afterSkillsFilteredList, job)
            else:
                lt.changeInfo(afterSkillsFilteredList, id_pos, job)
    
    countriesList = lt.newList('ARRAY_LIST')
    groupedByCountry = lt.newList('ARRAY_LIST')
    for newOffer in lt.iterator(afterSkillsFilteredList):
        pos_country = lt.isPresent(countriesList, newOffer['country_code'])
        if pos_country == 0:
            lt.addLast(countriesList, newOffer['country_code'])
            newItem = {'country_code': newOffer['country_code'],
                       'cant_offers': 0,
                       'junior': {'skills_dict': {},
                                  'acum_level': 0,
                                  'cont_level': 0,
                                  'companies_dict': {},
                                  'companies_dictByCity': {}},
                       'mid': {'skills_dict': {},
                               'acum_level': 0,
                               'cont_level': 0,
                               'companies_dict': {},
                               'companies_dictByCity': {}},
                       'senior': {'skills_dict': {},
                                  'acum_level': 0,
                                  'cont_level': 0,
                                  'companies_dict': {},
                                  'companies_dictByCity': {}}}
            newItem['country_code'] = newOffer['country_code']
            newItem['cant_offers'] = 1
            for skill in lt.iterator(newOffer['skills']):
                if skill not in newItem[newOffer['experience_level']]['skills_dict']:
                    newItem[newOffer['experience_level']]['skills_dict'][skill] = 1
                else:
                    newItem[newOffer['experience_level']]['skills_dict'][skill] += 1
            newItem[newOffer['experience_level']]['acum_level'] += newOffer['acum_level']
            newItem[newOffer['experience_level']]['cont_level'] += newOffer['cont_level']
            newItem[newOffer['experience_level']]['companies_dict'][newOffer['company_name']] = 1 
            newItem[newOffer['experience_level']]['companies_dictByCity'][newOffer['company_name']] = lt.newList('ARRAY_LIST')
            lt.addLast(newItem[newOffer['experience_level']]['companies_dictByCity'][newOffer['company_name']], newOffer['city'])
            lt.addLast(groupedByCountry, newItem)
        else:
            itemToUpdate = lt.getElement(groupedByCountry, pos_country)
            itemToUpdate['cant_offers'] += 1
            for skill in lt.iterator(newOffer['skills']):
                if skill not in itemToUpdate[newOffer['experience_level']]['skills_dict']:
                    itemToUpdate[newOffer['experience_level']]['skills_dict'][skill] = 1
                else:
                    itemToUpdate[newOffer['experience_level']]['skills_dict'][skill] += 1
            itemToUpdate[newOffer['experience_level']]['acum_level'] += newOffer['acum_level']
            itemToUpdate[newOffer['experience_level']]['cont_level'] += newOffer['cont_level']
            if newOffer['company_name'] not in itemToUpdate[newOffer['experience_level']]['companies_dict']:
                itemToUpdate[newOffer['experience_level']]['companies_dict'][newOffer['company_name']] = 1
            else:
                itemToUpdate[newOffer['experience_level']]['companies_dict'][newOffer['company_name']] += 1
            dict = itemToUpdate[newOffer['experience_level']]['companies_dictByCity']
            if newOffer['company_name'] not in dict:
                itemToUpdate[newOffer['experience_level']]['companies_dictByCity'][newOffer['company_name']] = lt.newList('ARRAY_LIST')
                lt.addLast(itemToUpdate[newOffer['experience_level']]['companies_dictByCity'][newOffer['company_name']], newOffer['city'])
            else:
                list = dict[newOffer['company_name']]
                lt.addLast(list, newOffer['company_name'])
            lt.changeInfo(groupedByCountry, pos_country, itemToUpdate)
            
    unorderedList = lt.newList("ARRAY_LIST")
    for country in lt.iterator(groupedByCountry):
        item = {'country_code': country['country_code'],
                'cant_offers': country['cant_offers'],
                'junior': lt.newList('ARRAY_LIST'),
                'mid': lt.newList('ARRAY_LIST'),
                'senior': lt.newList('ARRAY_LIST')}
        
        dictJunior = {'cont_skills': 0,
                      'max_skill': '',
                      'cont_maxSkill' : 0,
                      'min_skill': '',
                      'cont_minSkill': 0,
                      'prom_level': 0,
                      'cont_companies': 0,
                      'max_company': '',
                      'min_company': '',
                      'cant_más_sedes': 0}
        juniorSkillsDict = country['junior']['skills_dict']
        dictJunior['cont_skills'] = len(juniorSkillsDict)
        maxSJ = ''
        maxcontSJ = 0
        minSJ = ''
        mincontSJ = 1000000
        for skill in juniorSkillsDict:
            if juniorSkillsDict[skill] > maxcontSJ:
                maxSJ = skill
                maxcontSJ = juniorSkillsDict[skill]
            if juniorSkillsDict[skill] < mincontSJ:
                minSJ = skill
                mincontSJ = juniorSkillsDict[skill]
        dictJunior['max_skill'] = maxSJ
        dictJunior['cont_maxSkill'] = maxcontSJ
        dictJunior['min_skill'] = minSJ 
        dictJunior['cont_minSkill'] = mincontSJ if mincontSJ != 1000000 else 0
        dictJunior['prom_level'] = round((country['junior']['acum_level'] / country['junior']['cont_level']), 2) if country['junior']['cont_level'] != 0 else 0
        juniorCompaniesDict = country['junior']['companies_dict']
        dictJunior['cont_companies'] = len(juniorCompaniesDict)
        maxCJ = ''
        maxcontCJ = 0
        minCJ = ''
        mincontCJ = 1000000
        for company in juniorCompaniesDict:
            if juniorCompaniesDict[company] > maxcontCJ:
                maxCJ = company
                maxcontCJ = juniorCompaniesDict[company]
            if juniorCompaniesDict[company] < mincontCJ:
                minCJ = company
                mincontCJ = juniorCompaniesDict[company]
        dictJunior['max_company'] = maxCJ
        dictJunior['min_company'] = minCJ
        dictByCityJunior = country['junior']['companies_dictByCity']
        for company in dictByCityJunior:
            if lt.size(dictByCityJunior[company]) > 1:
                dictJunior['cant_más_sedes'] += 1
        lt.addLast(item['junior'], dictJunior)
        item['junior'] = tabulate(lt.iterator(item['junior']), tablefmt='grid', headers='keys', maxcolwidths=6)
        
        dictMid = {'cont_skills': 0,
                   'max_skill': '',
                   'cont_maxSkill' : 0,
                   'min_skill': '',
                   'cont_minSkill': 0,
                   'prom_level': 0,
                   'cont_companies': 0,
                   'max_company': '',
                   'min_company': '',
                   'cant_más_sedes': 0}
        midSkillsDict = country['mid']['skills_dict']
        dictMid['cont_skills'] = len(midSkillsDict)
        maxSM = ''
        maxcontSM = 0
        minSM = ''
        mincontSM = 1000000
        for skill in midSkillsDict:
            if midSkillsDict[skill] > maxcontSM:
                maxSM = skill
                maxcontSM = midSkillsDict[skill]
            if midSkillsDict[skill] < mincontSM:
                minSM = skill
                mincontSM = midSkillsDict[skill]
        dictMid['max_skill'] = maxSM
        dictMid['cont_maxSkill'] = maxcontSM
        dictMid['min_skill'] = minSM
        dictMid['cont_minSkill'] = mincontSM if mincontSM != 1000000 else 0
        dictMid['prom_level'] = round((country['mid']['acum_level'] / country['mid']['cont_level']), 2) if country['mid']['cont_level'] != 0 else 0
        MidCompaniesDict = country['mid']['companies_dict']
        dictMid['cont_companies'] = len(MidCompaniesDict)
        maxCM = ''
        maxcontCM = 0
        minCM = ''
        mincontCM = 1000000
        for company in MidCompaniesDict:
            if MidCompaniesDict[company] > maxcontCM:
                maxCM = company
                maxcontCM = MidCompaniesDict[company]
            if MidCompaniesDict[company] < mincontCM:
                minCM = company
                mincontCM = MidCompaniesDict[company]
        dictMid['max_company'] = maxCM
        dictMid['min_company'] = minCM
        dictByCityMid = country['mid']['companies_dictByCity']
        for company in dictByCityMid:
            if lt.size(dictByCityMid[company]) > 1:
                dictMid['cant_más_sedes'] += 1
        lt.addLast(item['mid'], dictMid)
        item['mid'] = tabulate(lt.iterator(item['mid']), tablefmt='grid', headers='keys', maxcolwidths=6)
        
        dictSenior = {'cont_skills': 0,
                      'max_skill': '',
                      'cont_maxSkill' : 0,
                      'min_skill': '',
                      'cont_minSkill': 0,
                      'prom_level': 0,
                      'cont_companies': 0,
                      'max_company': '',
                      'min_company': '',
                      'cant_más_sedes': 0}
        seniorSkillsDict = country['senior']['skills_dict']
        dictSenior['cont_skills'] = len(seniorSkillsDict)
        maxSS = ''
        maxcontSS = 0
        minSS = ''
        mincontSS = 1000000
        for skill in seniorSkillsDict:
            if seniorSkillsDict[skill] > maxcontSS:
                maxSS = skill
                maxcontSS = seniorSkillsDict[skill]
            if seniorSkillsDict[skill] < mincontSS:
                minSS = skill
                mincontSS = seniorSkillsDict[skill]
        dictSenior['max_skill'] = maxSS
        dictSenior['cont_maxSkill'] = maxcontSS
        dictSenior['min_skill'] = minSS
        dictSenior['cont_minSkill'] = mincontSS if mincontSS != 1000000 else 0
        dictSenior['prom_level'] = round((country['senior']['acum_level'] / country['senior']['cont_level']), 2) if country['senior']['cont_level'] != 0 else 0
        seniorCompaniesDict = country['senior']['companies_dict']
        dictSenior['cont_companies'] = len(seniorCompaniesDict)
        maxCS = ''
        maxcontCS = 0
        minCS = ''
        mincontCS = 1000000
        for company in seniorCompaniesDict:
            if seniorCompaniesDict[company] > maxcontCS:
                maxCS = company
                maxcontCS = seniorCompaniesDict[company]
            if seniorCompaniesDict[company] < mincontCS:
                minCS = company
                mincontCS = seniorCompaniesDict[company]
        dictSenior['max_company'] = maxCS
        dictSenior['min_company'] = minCS
        dictByCitySenior = country['senior']['companies_dictByCity']
        for company in dictByCitySenior:
            if lt.size(dictByCitySenior[company]) > 1:
                dictSenior['cant_más_sedes'] += 1
        lt.addLast(item['senior'], dictSenior)
        item['senior'] = tabulate(lt.iterator(item['senior']), tablefmt='grid', headers='keys', maxcolwidths=6)
        
        lt.addLast(unorderedList, item)
        
    orderedList = sa.sort(unorderedList, sortByCantOffers)
    
    if lt.size(orderedList) > numberOfOffersToShow:
        offersList = lt.subList(orderedList, 1, numberOfOffersToShow)
    else:
        offersList = orderedList
        
    totalOfertas = lt.size(offersList)        
    if totalOfertas > 6:
        listaOfertas = getFirstAndLast3(offersList)
    else:
        listaOfertas = offersList
        
    return lt.size(filteredList), lt.size(citiesList), {maxCountry: maxCo}, {maxCity: maxC}, listaOfertas 
            


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


def binary_search(list, low, high, element):
    if high >= low:
        mid = (high + low) // 2
        job = lt.getElement(list, mid)
        if job['id'] == element:
            return mid
        elif job['id'] < element:
            return binary_search(list, low, mid - 1, element)
        else:
            return binary_search(list, mid + 1, high, element)
    else:
        return -1
    

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


def sortByIdCriteria(data1, data2):
    return data1["id"] > data2["id"]

def sortByCantOffers(data1, data2):
    return data1["cant_offers"] > data2["cant_offers"]


def sortByDateAndComapnyCriteria(data1, data2):
    if data1["published_at"] > data2["published_at"]:
        return True
    elif data1["published_at"] == data2["published_at"]:
        if data1["company_name"] < data2["company_name"]:
            return True

    return False
    
    
def sortByDateAndCountryCriteria(data1, data2):
    if data1["published_at"] > data2["published_at"]:
        return True
    elif data1["published_at"] == data2["published_at"]:
        if data1["country_code"] < data2["country_code"]:
            return True

    return False
    
    
def sortByCantAndSalaryAndCityCriteria(data1, data2):
    if data1["cant_offers"] > data2["cant_offers"]:
        return True
    elif data1["cant_offers"] == data2["cant_offers"]:
        if data1['prom_salaries'] > data2['prom_salaries']:
            return True
        elif data1['prom_salaries'] == data2['prom_salaries']:
            if data1['city'] < data2['city']:
                return True
    
    return False
     

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass