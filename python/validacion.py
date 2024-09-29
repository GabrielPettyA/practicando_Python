
import os

def validar():
  while True:
    try:
    
      ingreso = input("Desea continuar ? 'SI' o 'NO': ").upper()
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
      
      else:
        print("Seleccione --> 'SI' o 'NO'")
    
    except ValueError:
            print("\nERROR: Debe seleccionar entre 'SI' o 'NO' para continuar.")
