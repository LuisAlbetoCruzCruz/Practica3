import csv
nombre = []
apellido = []
edad = []
grado = []
grupo = []
correo = []
lista = []
apellidoM =[]

def menu():
  option = input("""
  
  [?] ELIGE UNA OPCION:
 
  1. REGISTRAR ALUMNO
  2. GUARDAD Y SALIR
  > """)
  if option == "1":
    nombre.append(input("Ingresa el Nombres:   "))
    apellido.append(input("Ingresa el Apellido Paterno:   "))
    apellidoM.append(input("Ingresa el Apellido Materno:   "))
    edad.append(input("Ingresa la Edad:   "))
    grado.append(input("Ingresa el Grado:   "))
    grupo.append(input("Ingrese el Grupo:   "))
    correo.append( input("ingresa el Correo:   "))
    return menu()

  if option == "2":
    lista = list(zip(nombre, apellido,apellidoM ,edad,grado,grado,correo))
    with open('alumnos.csv','w', newline= '') as file:
      writer = csv.writer(file, delimiter =',')
      writer.writerows(lista)
      print("""[✓] Estudiante creado....""")
      print("Guardado exitosamente")
      print("[X] ARCHIVO CERRADO")
    exit(0)
menu()