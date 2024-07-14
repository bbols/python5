import os
import shutil

def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Папка {folder_name} создана.")
    except FileExistsError:
        print("Такая папка уже существует.")

def delete_item(item_name):
    try:
        if os.path.isfile(item_name):
            os.remove(item_name)
            print(f"Файл {item_name} удален.")
        elif os.path.isdir(item_name):
            shutil.rmtree(item_name)
            print(f"Папка {item_name} удалена.")
        else:
            print("Такого файла или папки не существует.")
    except Exception as e:
        print(f"Ошибка: {e}")

def copy_item(source_name, destination_name):
    try:
        if os.path.isfile(source_name):
            shutil.copy(source_name, destination_name)
            print(f"Файл {source_name} скопирован как {destination_name}.")
        elif os.path.isdir(source_name):
            shutil.copytree(source_name, destination_name)
            print(f"Папка {source_name} скопирована как {destination_name}.")
        else:
            print("Такого файла или папки не существует.")
    except Exception as e:
        print(f"Ошибка: {e}")

def list_items():
    items = os.listdir()
    print('\n'.join(item for item in os.listdir()) if items else 'Рабочая директория пуста.')


def list_folders():
    items = os.listdir()
    folders = [item for item in items if os.path.isdir(item)]
    print("\n".join(folder for folder in folders) if folders else "В рабочей директории нету папок")

def list_files():
    items = os.listdir()
    files = [item for item in items if os.path.isfile(item)]
    print("\n".join(file for file in files) if files else "в рабочей директории нету файлов")
