
# Importación de los módulos requeridos.

import os
import solicitud_datos


# Inicio de la función.

def validar():
  
  # Se utiliza el bucle while siempre y cuando su valor sea True.
  while True:
    try:
    
      ingreso = input("Desea continuar ? 'SI', 'NO' u 'OTRO': ").upper()
      
      if ingreso == 'SI':
        return True
      
      if ingreso == 'NO':
        os.system('cls')        
        print("Gracias por utilizar el sistema")
        print(f'''
              Cerrando...
              ...EXIT.
              '''
              )
        exit() ### Función para salir de función en terminal. ###
        return False
      
      if ingreso == 'OTRO':
        os.system
        solicitud_datos.datos() ### Se llama al archivo con la función de carga de datos desde esta posición. ###
        print("Gracias por utilizar el sistema")
        print(f'''
              Cerrando...
              ...EXIT.
              '''
              )
        exit()
      
      # Se captura el ERROR en caso de no ingresar opción requerida.
      else:
        print("Seleccione --> 'SI' o 'NO'")
    
    # Se captura el ERROR en caso de aceptar con 'ENTER' sin haber cargado dato previo.
    except ValueError:
            print("\nERROR: Debe seleccionar entre 'SI' o 'NO' para continuar.")
