import os
import json
import hashlib

path = '/Users/milton/Desktop/proyecto_gitfit/gitfit'

# Directorio de archivos

def file_listing(path:str) -> list:
    # ignoring_files = file_reading_lines(path + '.gitignore')
    # files_to_ignore = [file_name[:-1] for file_name in ignoring_files]
    # all_files = os.listdir(path)
    # files = []

    # for file in all_files:
    #     if file not in files_to_ignore:
    #         files.append(file)


    return os.listdir(path)
    
def file_reading(path:str) -> str:
    with open(path, 'r') as reader:
        return reader.read()

def file_reading_lines(path:str) -> list:
   with open(path, 'r') as reader:
        return reader.readlines() 

# ENCRIPTACION DE ARCHIVOS (HASHING FILES PERO ASI SUENA MAS COOL)

def hash_files(path:str) -> str:
    file_text = file_reading(path)
    file_hash = hashlib.sha1(file_text.encode('utf-8')).hexdigest()
    return file_hash

def get_hash_dictionary (path:str) -> dict:    
    files = file_listing(path)
    hash_collection = {}
    for file in files:
        hash_collection[file] = hash_files(path + file)
    return hash_collection

def save_hash_dictionary(path:str) -> None:
    with open(path + '.hashdict.json' , 'w') as writer:
        hash_dictionary = get_hash_dictionary(path)
        json.dump(hash_dictionary, writer)

    return None

def read_current_hash_dict (path:str) ->dict:
    with open(path + '.hashdict.json', 'r') as reader:
        file = reader.read()
        return json.loads(file)

# Escanners, estas son las funciones de gitfit ;)

def scanning_for_new_files (path:str) -> list:
    previous_files = read_current_hash_dict(path).keys()
    current_files = get_hash_dictionary (path).keys()
    new_files = []

    for file in current_files:
        if file not in previous_files:
            new_files.append(file)
    return new_files

def scanning_deleted_files(path:str) -> list:
    previous_files = read_current_hash_dict(path).keys()
    current_files = get_hash_dictionary (path).keys()
    deleted_files = []

    for file in previous_files:
        if file not in current_files:
            deleted_files.append(file)

    return deleted_files

def scanning_modified_files(path:str) -> list:
    previous_hash_dictionary = read_current_hash_dict(path)
    current_hash_dictionary = get_hash_dictionary (path)
    previous_files = read_current_hash_dict(path).keys()
    current_files = get_hash_dictionary (path).keys()
    modified_files = []

    for file in current_files:
        if file not in previous_files:
            if previous_hash_dictionary[file] != current_hash_dictionary[file]:
                modified_files.append(file)

    return modified_files


print('New Files: ', scanning_for_new_files(path))
