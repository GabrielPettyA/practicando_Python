import os

def datos():
  os.system('cls')
  list_data = []
    
  name = input("\nIngrese Nombre: ")
  list_data.append(name)
  
  age = int(input("Ingrese su edad: "))
  list_data.append(age)
  
  street = input("Ingrese nombre de calle: ")
  list_data.append(street)
  
  num = int(input("Ingrese altura: "))
  list_data.append(num)
  
  print(f'''{os.system('cls')}
        Datos Ingresados:
        
                Nombre: {name}
                Edad  : {age}
                Calle : {street}
                Altura: {num}
        '''
        )
  
  
  print("Datos guardados en lista:\n")
  print(list_data,'\n')

