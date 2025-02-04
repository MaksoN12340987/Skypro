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

# поиск позиции первого вхождения подстроки в строку
string.index(substring)                             
                            
# колличество вхождений элементов                   
string.count(element)                              
                    
# перевод в нижний регистр                          
string.lower()                                      
                            
# перевод в верхний регистр                        
string.upper()                                      
                            
# чтобы все слова начинались с большой буквы  
string.title()

# замена элементов строки
string.replace(old_substring, new_substring)

# состоит ли каждый символ строки из цифр (0–9)
string.isdigit()   "10 24".isdigit() >>>  False

#  каждый символ строки из букв
"кусь".isalpha()  >>>  True

# создать список из строки
string.split()
                                                            


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


<!-- Module typing -->
# Union переменную с несколькими возможными типами
def foo(arg: Union[str, int]) -> None:

# Any переменная может иметь любой тип
def foo(arg: Any) -> None:

# Optional переменная может иметь значение None
def foo(arg: Optional[int] = None) -> None:
# or: 
def foo(arg: int | None) -> None:

# Iterable переменная является итерируемым объектом, например list, tuple, set или dict
def foo(arg: Iterable[int]) -> None:

# Callable для объектов, которые являются вызываемыми (со скобками), например любая функция
def foo(func: Callable, array: Iterable[int]) -> None:


# PYTEST

pytest --cov=src --cov-report=html


<!-- GIT -->
# --cached — команда удалит файл только из индекса, но оставит его в вашем рабочем каталоге (файл сохранится на диске):
git rm --cached filename

# список всех выполненных коммитов, отсортированных по дате добавления
git log

# oткатить изменения до определённого коммита и нечего не сломать:
git reset --mixed "commit_ID"

# все изменения, сделанные в рамках одного коммита
git show

# У команды 
git log
#  есть ряд полезных флагов, которые помогают выводить:

--all — все ветки и теги.

--oneline — каждый коммит на одну строку.

--decorate — информацию, на какие ветки ссылается каждый коммит.

--graph — графические связи между коммитами.

--p — разницу между коммитами (выводит информацию об изменениях для каждого коммита).

--author=name — только коммиты, сделанные указанным автором.

--since=date — только коммиты, сделанные после указанной даты.

--until=date — только коммиты, сделанные до указанной даты.

--grep=pattern — только коммиты, содержащие указанный паттерн (шаблон) в сообщении коммита, то есть отображает только те коммиты, у которых в сообщении есть то, что мы укажем как pattern

--file_name — коммиты, которые изменяют указанный файл.
