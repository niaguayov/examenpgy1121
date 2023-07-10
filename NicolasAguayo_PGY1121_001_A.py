import os
os.system("cls")

import datetime

 ###GITHUB: https://github.com/niaguayov/examenpgy1121

asientos=[True]*100
asistentes=["rut","nombre","apellido"]
entradastotales=[0,0,0]
precio=0

def reservaentrada():
            rut=input("Ingrese su rut sin puntos ni guion: ")
            nombre=input("Ingrese su nombre: ")
            apellido=input("Ingrese su apellido: ")
            asistentes[0]=rut
            asistentes[1]=nombre
            asistentes[2]=apellido

def reservaasiento():
     for asiento in range(len(asientos)):  
        if asientos[asiento]==True:
            print(f"Estos son los asientos disponibles: Asiento {asiento+1}")
            asientos[asiento]==False
            estado="Esta Disponible"
            print(f"El asiento Se ha reservado con exito.")
        elif asientos[asiento]==False:
            estado="No esta disponible"
            print(f"El asiento no esta disponible.")
            

def mostrarubicaciones():
    for asiento in range(len(asientos)):
        print(f"Lista de todos los asientos: Asiento {asiento+1}")

def mostrarasistentes():
        print(f"{asistentes}")


while True:

    opcion=input("""\nConcierto Michael Jam

1-Comprar Entrada
2-Mostrar Ubicaciones Disponibles
3-Ver Listado Asistentes
4-Mostrar Ganancias Totales
5-Salir

opcion: """)

    match opcion:
        case "1":
            while True:
                cantidadentradas=int(input("Cuantas entradas desea reservar?: "))
                if cantidadentradas<4 and cantidadentradas>0:
                    opcion=input(""""Que entrada desea comprar?
                1- Platinum
                2-Gold
                3-Silver
                Opcion: """)
                    
                    if opcion=="1":
                        precio=120000
                        entradastotales[0]=cantidadentradas
                        print(f"Usted ha comprado {cantidadentradas} entradas Platinum, valor {precio}")
                    elif opcion=="2":
                        precio=80000
                        entradastotales[1]=cantidadentradas
                        print(f"Usted ha comprado {cantidadentradas} entradas gold, valor {precio}")
                    
                    elif opcion=="3":
                        precio=50000
                        entradastotales[2]=cantidadentradas
                        print(f"Usted ha comprado {cantidadentradas} entradas silver, valor {precio}")

                    else:
                        print("Ingrese una opcion valida.")

                    reservaentrada()
                else:
                    print("Debe ingresar un valor, y este no puede sobrepasar las 3 entradas")
                break

        case "2":
            while True:
                mostrarubicaciones
                break

        case "3":
            while True:
                mostrarasistentes()
                break

        case "4":
            while True:
                print(entradastotales)
                total=(entradastotales[0]*120000)+(entradastotales[1]*80000)+(entradastotales[2]*50000)
                print(f"""Se compraron un total de:
                1-Entradas Platinum, cantidad {entradastotales[0]}, total {entradastotales[0]*120000}
                2-Entradas Gold, cantidad {entradastotales[1]}, total {entradastotales[1]*80000}
                2-Entradas Silver, cantidad {entradastotales[2]}, total {entradastotales[2]*50000}
                """)
                print(f"El costo total sera de {total}")
                break

        case "5":
            print(f"Gracias por su compra {asistentes[1]}{asistentes[2]}")
            print("Saliendo del programa...")
            break
