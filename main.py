import os
import shutil
import platform
from file_manager import create_folder, delete_item, copy_item, list_items, list_folders, list_files
from quiz import play_quiz
from bank_account import manage_bank_account

def main_menu():
    print("\nМеню:")
    print("1. Создать папку")
    print("2. Удалить (файл/папку)")
    print("3. Копировать (файл/папку)")
    print("4. Просмотр содержимого рабочей директории")
    print("5. Посмотреть только папки")
    print("6. Посмотреть только файлы")
    print("7. Просмотр информации об операционной системе")
    print("8. Создатель программы")
    print("9. Играть в викторину")
    print("10. Мой банковский счет")
    print("11. Смена рабочей директории (необязательный пункт)")
    print("12. Выход")

def main():
    while True:
        main_menu()
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            folder_name = input("Введите название папки: ")
            create_folder(folder_name)
        elif choice == '2':
            item_name = input("Введите название файла или папки для удаления: ")
            delete_item(item_name)
        elif choice == '3':
            source_name = input("Введите название файла или папки для копирования: ")
            destination_name = input("Введите новое название файла или папки: ")
            copy_item(source_name, destination_name)
        elif choice == '4':
            list_items()
        elif choice == '5':
            list_folders()
        elif choice == '6':
            list_files()
        elif choice == '7':
            print(platform.system(), platform.release())
        elif choice == '8':
            print("Создатель программы: Ваше Имя")
        elif choice == '9':
            play_quiz()
        elif choice == '10':
            manage_bank_account()
        elif choice == '11':
            new_directory = input("Введите полный или относительный путь: ")
            try:
                os.chdir(new_directory)
                print(f"Текущая рабочая директория: {os.getcwd()}")
            except FileNotFoundError:
                print("Неверный путь.")
        elif choice == '12':
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню")

if __name__ == "__main__":
    main()
