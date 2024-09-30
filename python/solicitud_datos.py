
# Importación de módulo para limpiar terminal de datos cargados con anterioridad.

import os

# Inicio de función.

def datos():
  os.system('cls')
  list_data = [] ### Lista vacía para registrar los datos ingresados. ###
  
  # Ingreso de datos por usuario.
  
  name = input("\nIngrese Nombre: ").title()
  list_data.append(name) ### Se agregan los datos ingresados en la lista. ###
  
  age = int(input("Ingrese su edad: ")).title()
  list_data.append(age)
  
  street = input("Ingrese nombre de calle: ").title()
  list_data.append(street)
  
  num = int(input("Ingrese altura: "))
  list_data.append(num)
  
  
  # Impresión de los datos directamente de las variables del input.
  
  print(f'''{os.system('cls')}
        Datos Ingresados:
        
                Nombre: {name}
                Edad  : {age}
                Calle : {street}
                Altura: {num}
        '''
        )
  
  
  # Obtención de los datos registrados en la lista, directamente de la lista.
  
  print("Datos guardados en lista:\n")
  print(list_data,'\n')

# Fin de función.
