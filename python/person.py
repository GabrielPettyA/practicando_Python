### CLASS PERSON ###

# Se importan los módulos requeridos

import os
import validacion

# Inicio de la Clase Person, la misma presenta un constructor con sus respectivos atributos.
class Person:
  
  def __init__(self, nombre= "Null", edad= "Null", Dni= "Null"):
    self.nombre = nombre
    self.edad = edad
    self.Dni = Dni

# Se solicita al usuario el ingreso de las cantidades de personas a registrar.

#person = int(input("Cantidad de personas por ingresar: "))

# Contador de personas ingresadas a registrar.
person = 1
contar = 0

# Inicio del bucle for para permitir el registro de la cantidad de personas autorizadas.
for ind in range(person):
  if person :
    
    #nombre = input("Ingrese Nombre: ")
    nombre = 'Gabriel'
    #edad = int(input("Ingrese Edad: "))
    edad = 50
    #dni = int(input("Ingrese DNI: "))
    dni = 23766454
    contar =+1

    persona_1 = Person(nombre=nombre, edad=edad, Dni=dni)

# Se imprime el resultado obtenido de los registros.
    print(f''' 
          ================================
          DATE PERSON
          Nombre   : {persona_1.nombre}
          Edad     : {persona_1.edad} años
          DNI      : {persona_1.Dni}
          ================================
          ''')
  #Fin de bucle for.
  
print("Ingreso ==> ", person, "personas")

print("\n ---------------------- Proceso Finalizado ... ---------------------- \n")

os.system('cls')

# Inicio de nueva función y el registro mediante el diccionario.
def nuevo():
  my_dict = dict(primero='Gabriel', segundo='Alejandro', tercero='Pettinari', cuarto='50 años')
  
  # Imprimiendo los datos en el diccionario.
  
  print(f'''
        Datos del Diccionario:
        
        {my_dict}
        '''
        )
  
# Otras formas de imprimir la información del diccionario.

  print("Buscando datos específicos: ", f'''
        Primer dato con clave primero  - {my_dict['primero']}
        Segundo dato con clave segundo - {my_dict['segundo']}
        Tercer dato con clave tercero  - {my_dict['tercero']}
        Cuarto dato con clave cuarto   - {my_dict['cuarto']}
        '''
        )

  print(f''' 
        Otra forma...
        
        Datos con claves primero y segundo  - {my_dict['primero']} {my_dict['segundo']}

        Datos con claves tercero y cuarto   - {my_dict['tercero']}; {my_dict['cuarto']}

        '''
        )

  print(f'''Elija número de clave:
        
        1 (primero), 
        2 (segundo),
        3 (tercero),
        4 (cuarto)
        '''
        )


# Inicio del bucle while para validación de ingreso de opciones.

  while True:
    
    # Utilización de try para validar los diversos ingresos y capturar los posibles errores.
      try:
        
        ingreso = int(input("\nIngrese opción: "))
        os.system('cls')
        if ingreso <1 or ingreso >4 :
          print("\nERROR: Ingrese Clave entre 1 y 4.")
    
    # Se disponen en las opciones el archivo de validación, el llamado nos redirige al mismo para 
    # poder hacer las validaciones correspondientes.
    
        if ingreso == 1:
          print("\nClave 1: ", my_dict['primero'])
          validacion.validar() ### Llama al archivo previamente importado. ###
          
        if ingreso == 2:
          print("\nClave 2: ", my_dict['segundo'])
          validacion.validar()
                      
        if ingreso == 3:
          print("\nClave 3: ", my_dict['tercero'])
          validacion.validar()
                      
        if ingreso == 4:
          print("\nClave 4: ", my_dict['cuarto'])
          validacion.validar()
                    
        else:
          pass                
    
    
    # Captura del ValueError para poder determinar una acción a seguir.
    # Sirve para capturar el accionar del usuario al apretar 'ENTER' sin
    # haber ingresado dato previo.
    
      except ValueError:
        os.system('cls')
        
        print(f'''
              ERROR: 
                  Ingrese clave solicitada para continuar.
                  1, 2, 3 o 4
                  ''')


nuevo()

# Fin de funcion.

## ================================================================ ##

  
  