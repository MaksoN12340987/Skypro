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

<!-- ///   STRING   /// -->

# поиск позиции первого вхождения подстроки в строку        # замена элементов строки
string.index(substring)                                     string.replace(old_substring, new_substring)
                                                            
# колличество вхождений элементов                           # состоит ли каждый символ строки из цифр (0–9)
string.count(element)                                       string.isdigit()   "10 24".isdigit() >>>  False
                                                            
# перевод в нижний регистр                                  #  каждый символ строки из букв
string.lower()                                              "кусь".isalpha()  >>>  True
                                                            
# перевод в верхний регистр                                 
string.upper()                                              
                                                            
# чтобы все слова начинались с большой буквы                
string.title()                                              
                                                            

