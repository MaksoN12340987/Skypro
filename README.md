# Skypro
Lessons in Skypro, Python dewalopment

<!-- Математичемкие операции -->

Целочисленное деление //
Остаток от деления %
Возведение в степень **
Инкремент +=
Декремент -=

# есть ли в "а" значение "b"
a in b 

print(f"string{war}")

str() — строка

float() — дробное число

round() — округляет число

<!-- ///   LISTS   /// -->

# добавление элемента в список при этом после него элементы i++
list.insert(index, element) 

# позволяет вернуть индекс
index = my_list.index(3) 
list.index(element_to_find, start_index, end_index) '''не включая end_index'''
print(index)

# колличество элементов
list.count(element)

# Удалите последний элемент
list.pop()

# для объединения двух списков
list_1.extend(list_2)

<!-- ///   STRING   /// -->

# поиск позиции первого вхождения подстроки в строку        # замена элементов строки
string.index(substring)                                     string.replace(old_substring, new_substring)
                                                            
# колличество вхождений элементов                           # состоит ли каждый символ строки из цифр (0–9)
string.count(element)                                       string.isdigit()   "10 24".isdigit() >>>  False
                                                            
# перевод в нижний регистр                                  #  каждый символ строки из букв
string.lower()                                              "кусь".isalpha()  >>>  True
                                                            
# перевод в верхний регистр                                 # создать список из строки
string.upper()                                              string.split()
                                                            
# чтобы все слова начинались с большой буквы                
string.title()                                              
                                                            


<!-- virtual environment -->

# Create Windows
python -m venv venv
# Linux, macOS
python3 -m venv venv

# Function
# возвращает текущую рабочую директорию в виде строки
= os.getcwd()

# возвращает список файлов и директорий в указанной директории
= os.listdir('/path/to/directory')

# объединения путей
joined_path = os.path.join(path1, path2)

# дирректория расположения файла
 = os.path.dirname('/path/to/directory/file.txt')  >>>  /path/to/directory

# функция для работы с файлами
 file = open('example.txt', 'r')   ***   'r' — режим открытия файла на чтение

 file.close()

# читает весь файл целиком:
content = file.read()

# читает одну строку за раз:
line = file.readline()

# читает все строки и возвращает их в виде списка:
lines = file.readlines()

# запись
file.write('Hello, World!')


# Контекстный менеджер
# если файл уже существует, его содержимое будет безвозвратно потеряно при открытии в режиме 'w'
with open('example.txt', 'r') as file:   ***   'r' — режим открытия файла на чтение
    content = file.read()                ***   'w' — открывает файл для записи
    print(content)                       ***   'a' — открывает файл для добавления данных

# Режим чтения и записи 'r+'
with open('example.txt', 'r+') as file:
    content = file.read()
    file.write('\nNew content')

# Режим двоичного чтения 'rb'
# Такой подход часто применяется при работе с файлами, содержащими изображения, аудио, видео, 
# сжатые данные, и другими типами файлов, которые не предназначены для текстового представления


