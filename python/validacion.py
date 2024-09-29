
import os
import solicitud_datos

def validar():
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
        exit()
        return False
      
      if ingreso == 'OTRO':
        os.system
        solicitud_datos.datos()
        print("Gracias por utilizar el sistema")
        print(f'''
              Cerrando...
              ...EXIT.
              '''
              )
        exit()
        return True
      
      else:
        print("Seleccione --> 'SI' o 'NO'")
    
    except ValueError:
            print("\nERROR: Debe seleccionar entre 'SI' o 'NO' para continuar.")
