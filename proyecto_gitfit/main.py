import os


with open('data.txt', 'r') as f:
    data = f.read()
    print(data)

with open('data.txt', 'w') as f:
    data = 'El kenny es un cule hueco'
    print(data)

#Nos imprime el directoerio (en pocas palabras xd)
with os.scandir('/Users/milton/Desktop/proyecto_gitfit') as entries:
    for entry in entries:
        print(entry.name)

print('########################')
# List all files in a directory using os.listdir
basepath = '/Users/milton/Desktop/proyecto_gitfit'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

