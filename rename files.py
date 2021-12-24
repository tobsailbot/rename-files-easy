import os

# Rename files and add or delete words to name automatically:

def delete_file_name(folder, delete_name, file_ext):
    for folder, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            file_path = os.path.join(folder, name)
            if file_path.endswith(file_ext):
                file_name_index = file_path.find(delete_name)  # devuelve el indice de la primera letra de la string que encontró
                file_new_path = file_path[:file_name_index] + file_path[file_name_index + len(delete_name):]
            os.renames(file_path, file_new_path)


def rename_file(folder, new_name, file_ext):
    for folder, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            file_path = os.path.join(folder, name)
            if file_path.endswith(file_ext):
                path_reverse = (file_path[::-1])
                file_name = (path_reverse[:path_reverse.find(f'\\')])[::-1]
                file_new_path = (path_reverse[path_reverse.find(f'\\'):])[::-1] + new_name + file_name
            os.renames(file_path,file_new_path)


# This function deletes words from file's name:
 #   delete_file_name(folder, delete_name, file_ext)
#delete_file_name(r'D:\TOBI-PC\Descargas\Rare Sample pack - copia','Capital DK - ','wav')

rename_file(r'D:\TOBI-PC\Descargas\Rare Sample pack - copia','Tobsa-Kit - ','wav')

# This function add words at the start of file's name:
 #  rename_file(folder, new_name, file_ext)
# rename_file(folder, new_name, file_ext)
