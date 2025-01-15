import os

def change_names(directory_path, prefix):
    files = os.listdir(directory_path)  # Lista todos los archivos en el directorio especificado.
    for counter, file_name in enumerate(files):  # Itera sobre los archivos con un contador.
        name, extension = os.path.splitext(file_name)  # Divide el nombre del archivo y su extensión.
        new_name = f'{prefix}_{counter}{extension}'  # Crea el nuevo nombre usando el prefijo y el contador.
        os.rename( os.path.join(directory_path, file_name), os.path.join(directory_path, new_name) )
print('Cambios de nombre realizados')  # Imprime un mensaje de éxito

directory_path =r'agregar ruta'
prefix = 'agregar nuevo nombre '

change_names(directory_path,prefix)