import os

# with open('data.txt', 'r') as f:
#     data = f.read()
#     print(data)

# with open('data.txt', 'w') as f:
#     data = 'El kenny es un cule hueco'
#     print(data)

print('\nDirectorio de archivos de la carpeta:\n')

with os.scandir('/Users/milton/Desktop/proyecto_gitfit/gitfit/proyecto_gitfit') as entries:
    for entry in entries:
        print(entry.name)