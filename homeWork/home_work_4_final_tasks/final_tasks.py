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
