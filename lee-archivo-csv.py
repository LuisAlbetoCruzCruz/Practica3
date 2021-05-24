import csv
with open ('alumnos.csv') as f:
  reader = csv.reader(f,delimiter=",")
  for row in reader:
    print("NOMBRE: {0}, APELLIDO PATERNO: {1},  APELLIDO MATERNO: {2}, EDAD: {3}, GRADO: {4}, GRUPO: {5}, CORREO: {6}"
          .format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))