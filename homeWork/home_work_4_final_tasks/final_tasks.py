# Напишите функцию count_morse_characters(), которая принимает строку, состоящую из символов азбуки Морзе, и 
# возвращает количество символов (точек и/или тире) в ней
# def count_morse_characters(input_string):

#     point_counter = 0
#     dash_counter = 0
#     for i in range(len(input_string)):
#         if input_string[i] == ".":
#             point_counter += 1
        
#         else:
#             continue
    
#     return (point_counter + dash_counter)


# string_morse = input().replace(" ", "")
# print(count_morse_characters(string_morse))


# Создайте функцию morse_encode(), которая принимает словарь с азбукой Морзе и слово для кодирования 
# и возвращает его представление в азбуке Морзе с использованием пробелов между символами
# morse = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
#              "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
#              "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
#              "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
#              "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--",
#              "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

# words_to_decode = ['java', 'python', 'ruby', 'php', 'fortran', 'javascript', 'kotlin', 'swift', 'basic', 'pascal']

# def morse_encode(dictionary, word):
#     finaly = ""
#     for i in range(len(word)):
#         finaly += dictionary[word[i]] + " "
#     return finaly

# print(morse_encode(morse, words_to_decode[0]))


# Вам предоставлен словарь соответствия символов строки коду азбуки Морзе.
# Напишите функцию morse_decode(), которая принимает словарь с азбукой Морзе и строку в виде азбуки Морзе
#  и возвращает декодированное слово. Символы в закодированной строке разделены пробелами
# def morse_decode(dictionary, word):
#     list_word = list(word.split(" "))
#     keys_dict = list(dictionary.keys())
#     finaly = ""
#     for i in range(len(list_word)):
#         for count in range(len(keys_dict)):
#             if list_word[i] == dictionary[keys_dict[count]]:
#                 finaly += keys_dict[count]
#             else:
#                 continue
#     return finaly


# Напишите функцию calculate_total_cost(), которая принимает список продуктов 
# и возвращает общую стоимость всех товаров (цена * количество).
# Если у продукта не указаны цена и/или количество, это не должно приводить к ошибке.
products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25}
]

# def calculate_total_cost(ist_products):
#     total_prise = 0
#     prise = 0
#     quantity = 0

#     for i in range(len(ist_products)):
#         keys_list = list(ist_products[i].keys())
#         for index in range(len(keys_list)):
#             if keys_list[index] == "price":
#                 prise = ist_products[i][keys_list[index]]
#                 print(prise)
#             elif keys_list[index] == "quantity":
#                 quantity = ist_products[i][keys_list[index]]
#                 print(quantity)
                
#         if prise == 0:
#             prise = 1
#         elif quantity == 0:
#             quantity = 1
#         elif prise == 0 and quantity == 0:
#             continue
#         if prise != 0 and quantity != 0:
#             total_prise += prise * quantity

#     return total_prise

# print(calculate_total_cost(products))


# Напишите функцию filter_products_by_price(), которая принимает на вход список продуктов и верхний порог цены и 
# возвращает список продуктов, цена которых не превышает заданную максимальную цену. Если у продукта не указана цена, 
# это не должно приводить к ошибке, при получении значения по ключу, 
# если ключа в словаре нет - цена должна равняться 0 (используйте метод get())
# def filter_products_by_price(ist_products, maximum_price):
#     finaly_list = []
#     for i in range(len(ist_products)):
#         if ist_products[i].get("price", 0) <= maximum_price:
#             finaly_list.append(ist_products[i])
#     return finaly_list
                

# print(filter_products_by_price(products, 170))


# Напишите функцию find_product_by_name(), которая принимает список продуктов и имя для поиска и 
# возвращает информацию о продукте по его имени. Если продукт не найден в списке, 
# функция возвращает строку «Продукт с таким именем не найден в списке». 
# Если у продукта отсутствует имя, это не должно привести к ошибке
# def find_product_by_name(ist_product, name_product):
#     final = None
#     for i in range(len(ist_product)):
#         if ist_product[i].get("name", 0) == name_product:
#             final = ist_product[i]
#     if final:
#         return final
#     else:
#         return "Продукт с таким именем не найден в списке"
        
# print(find_product_by_name(products, "Carro"))


# Напишите функцию update_product_info(), которая обновляет информацию о продукте по его имени и 
# возвращает обновленный список продуктов.
# Функция принимает следующие аргументы: список продуктов, имя продукта, информацию, 
# по которому нужно обновить, и словарь с данными, которые требуется обновить. 
# За один вызов функция может обновить только один продукт. Если продукт не найден в списке, 
# функция возвращает строку «Продукт с таким именем не найден в списке».
# Если у продукта отсутствует имя, это не должно привести к ошибке
products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

def update_product_info(ist_product, name_product, dict_data):
    dict_find_humber = None
    final = {}
    
    for i in range(len(ist_product)):
        if ist_product[i].get("name", 0) == name_product:
            dict_find_humber = i
    
    if len(dict_data) <= len(ist_product[dict_find_humber]):
        key_product = 0
        key_find = 0
        for couht in range(len(dict_data)):
            final[].add(element)
    else:
        couht = len(ist_product[dict_find_humber])
    
    