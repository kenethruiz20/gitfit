import os
#import pandas as pd

# with open('data.txt', 'r') as f:
#     data = f.read()
#     print(data)

# with open('data.txt', 'w') as f:
#     data = 'El kenny es un cule hueco'
#     print(data)

list_of_files=os.listdir()
list_of_files.append('files.csv')

pd.DataFrame({'files':list_of_files}).to_csv('files.csv')

print('\nBienvenido a Git Fit =)\n')
print('Elija la operacion que desea realizar:')
print('1) DIRECTORIO DE ARCHIVOS')
print('2) AGREGAR ARCHIVOS DE TEXTO')
menu_option = int(input('\nIngrese: '))

if menu_option == 1:
    # print('\nDirectorio de archivos de la carpeta:\n') 
    # basepath = ''
    # with os.scandir('/Users/milton/Desktop/proyecto_gitfit/gitfit') as entries:
    #     for entry in entries:
    #         print(entry.name)
    for path, currentDirectory, files in os.walk("/Users/milton/Desktop/proyecto_gitfit/gitfit"):
        for file in files:
            print(file)

if menu_option == 2:
    with open('readme.txt', 'w') as f:
        user_text = str(input(''))
        f.write(user_text)
        print(user_text)

    
'''
Aca lo que hay que hacer es un menu
que importe las funciones del otro archivo
que el usuario elija que funcion utilizar
en el init tiene que ejecutar las cosas
o sea tiene que ejecutar el main
\
'''