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

import threading
import traceback
from tabulate import tabulate
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf

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
    # TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("-----------------------------------------")
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


def load_data():
    """
    Carga los datos
    
    """
    prefijo = input("Ingrese el prefijo de los archivos con que va a trabajar:\n")
    jobsSize = controller.load_data(control, prefijo)
    jobsList = controller.getFirstAndLast3Jobs(control)

    print("\nLoading data...\n")
    print("-------------------------------------")
    print("Total de ofertas de trabajo publicadaas cargadas: " + str(jobsSize))
    print("Printing the first 3 and last 3 records on file.\n")
    print(tabulate(lt.iterator(jobsList), tablefmt="grid", headers="keys"))

    print("\n\n")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    # TODO: Realizar la función para imprimir un elemento
    pass


def print_req_1():
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    pass


def print_req_2():
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    pass


def print_req_3():
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    numberOfOffersToShow = int(input(" Número (N) de ofertas a listar (ej.: 3, 5, 10 o 20): "))
    company = input("Nombre completo de la empresa a consultar: ")
    city = input("Ciudad de la oferta: ")
    
    print("\n======= Req No. 3 Inputs =========")
    print("Número de ofertas a listar: " + str(numberOfOffersToShow))
    print("Nombre completo de la empresa: " + company)
    print("Ciudad de la oferta: " + city)
    
    print("\n======= Req No. 3 Results =========")
    totalOfertas, listaOfertas, diff = controller.req_3(control, numberOfOffersToShow, company, city)
    print("Tiempor de ejecución del requerimiento: " + str(diff) + " [ms]")
    print("El total de ofertas ofrecidas por la empresa y ciudad es: " + str(totalOfertas))
    print(tabulate(lt.iterator(listaOfertas), tablefmt= "grid", headers= "keys"))


def print_req_4():
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    country = input("Código del país para la consulta (ej.: PL, CO, ES, etc): ")
    fechaInicio = input ("La fecha inicial del periodo a consultar (con formato '%Y-%m-%d'): ")
    fechaFinal = input("La fecha final del periodo a consultar (con formato '%Y-%m-%d'): ")
    
    print("\n======= Req No. 4 Inputs =========")
    print("País de consulta: " + country)
    print("Fecha inicial: " + fechaInicio)
    print("Fecha final: " + fechaFinal)
    
    print("\n======= Req No. 3 Results =========")
    totalOfertas, totalEmpresas, totalCiudades, ciudadMayor, ciudadMenor, listaOfertas, diff = controller.req_4(control, country, fechaInicio, fechaFinal)
    print("Tiempor de ejecución del requerimiento: " + str(diff) + " [ms]")
    print("El total de ofertas ofrecidas en el país y el periodo establecido es: " + str(totalOfertas))
    print("El total de empresas que publicaron al menos una oferta en el país es: " + str(totalEmpresas))
    print("Número de ciudades del país donde se publicaron ofertas: " + str(totalCiudades))
    print("Ciudad con el mayor número de ofertas y su conteo: " + ciudadMayor)
    print("Ciudad con el menor número de ofertas y su conteo: " + ciudadMenor)
    print(tabulate(lt.iterator(listaOfertas), tablefmt= "grid", headers= "keys"))


def print_req_5():
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    pass


def print_req_6():
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    pass


def print_req_7():
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()


def menu_cycle():
    """
    Menu principal
    """
    print("Bienvenido")
    working = True
    # ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar: ')

        if int(inputs) == 1:
            load_data()

        elif int(inputs) == 2:
            print_req_1()

        elif int(inputs) == 3:
            print_req_2()

        elif int(inputs) == 4:
            print_req_3()

        elif int(inputs) == 5:
            print_req_4()

        elif int(inputs) == 6:
            print_req_5()

        elif int(inputs) == 7:
            print_req_6()

        elif int(inputs) == 8:
            print_req_7()

        elif int(inputs) == 9:
            print_req_8()

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)


# main del reto
if __name__ == "__main__":
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()
