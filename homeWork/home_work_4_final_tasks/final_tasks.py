# Напишите функцию count_morse_characters(), которая принимает строку, состоящую из символов азбуки Морзе, и 
# возвращает количество символов (точек и/или тире) в ней
def count_morse_characters(input_string):
    point_counter = 0
    dash_counter = 0
    for i in range(len(input_string)):
        if input_string[i] == ".":
            point_counter += 1
        else:
            continue
    return (point_counter + dash_counter)


# Создайте функцию morse_encode(), которая принимает словарь с азбукой Морзе и слово для кодирования 
# и возвращает его представление в азбуке Морзе с использованием пробелов между символами
morse = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
             "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
             "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
             "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
             "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--",
             "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

words_to_decode = ['java', 'python', 'ruby', 'php', 'fortran', 'javascript', 'kotlin', 'swift', 'basic', 'pascal']

def morse_encode(dictionary, word):
    finaly = ""
    for i in range(len(word)):
        finaly += dictionary[word[i]] + " "
    return finaly


# Вам предоставлен словарь соответствия символов строки коду азбуки Морзе.
# Напишите функцию morse_decode(), которая принимает словарь с азбукой Морзе и строку в виде азбуки Морзе
#  и возвращает декодированное слово. Символы в закодированной строке разделены пробелами
def morse_decode(dictionary, word):
    list_word = list(word.split(" "))
    keys_dict = list(dictionary.keys())
    finaly = ""
    for i in range(len(list_word)):
        for count in range(len(keys_dict)):
            if list_word[i] == dictionary[keys_dict[count]]:
                finaly += keys_dict[count]
            else:
                continue
    return finaly


# Напишите функцию calculate_total_cost(), которая принимает список продуктов 
# и возвращает общую стоимость всех товаров (цена * количество).
# Если у продукта не указаны цена и/или количество, это не должно приводить к ошибке.
def calculate_total_cost(list_products):
    total_prise = 0
    prise = 0
    quantity = 0
    for i in range(len(list_products)):
        keys_list = list(list_products[i].keys())
        for index in range(len(keys_list)):
            if keys_list[index] == "price":
                prise = list_products[i][keys_list[index]]
                print(prise)
            elif keys_list[index] == "quantity":
                quantity = list_products[i][keys_list[index]]
                print(quantity)
        if prise == 0:
            prise = 1
        elif quantity == 0:
            quantity = 1
        elif prise == 0 and quantity == 0:
            continue
        if prise != 0 and quantity != 0:
            total_prise += prise * quantity
    return total_prise


# Напишите функцию filter_products_by_price(), которая принимает на вход список продуктов и верхний порог цены и 
# возвращает список продуктов, цена которых не превышает заданную максимальную цену. Если у продукта не указана цена, 
# это не должно приводить к ошибке, при получении значения по ключу, 
# если ключа в словаре нет - цена должна равняться 0 (используйте метод get())
products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

def filter_products_by_price(list_products, maximum_price):
    finaly_list = []
    for i in range(len(list_products)):
        if list_products[i].get("price", 0) <= maximum_price:
            finaly_list.append(list_products[i])
    return finaly_list


# Напишите функцию find_product_by_name(), которая принимает список продуктов и имя для поиска и 
# возвращает информацию о продукте по его имени. Если продукт не найден в списке, 
# функция возвращает строку «Продукт с таким именем не найден в списке». 
# Если у продукта отсутствует имя, это не должно привести к ошибке
def find_product_by_name(list_product, name_product):
    final = None
    for i in range(len(list_product)):
        if list_product[i].get("name", 0) == name_product:
            final = list_product[i]
    if final:
        return final
    else:
        return "Продукт с таким именем не найден в списке"


# Напишите функцию update_product_info(), которая обновляет информацию о продукте по его имени и 
# возвращает обновленный список продуктов.
# Функция принимает следующие аргументы: список продуктов, имя продукта, информацию, 
# по которому нужно обновить, и словарь с данными, которые требуется обновить. 
# За один вызов функция может обновить только один продукт. Если продукт не найден в списке, 
# функция возвращает строку «Продукт с таким именем не найден в списке».
# Если у продукта отсутствует имя, это не должно привести к ошибке
replace_dict = {"name": "REPLASE", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}

def update_product_info(list_product, name_product, dict_data):
    final = False
    for i in range(len(list_product)):
        if list_product[i].get("name", 0) == name_product:
            final = True
            keys_list = list(dict_data.keys())
            final = list_product[i]
            for count in range(len(dict_data)):
                list_product[i][keys_list[count]] = dict_data[keys_list[count]]
    if final:
        return list_product
    else:
        return "Продукт с таким именем не найден в списке"
    
  
#   Напишите функцию sort_products_by_quantity(). Функция должна принимать на вход список продуктов и 
# направление сортировки (атрибут должен иметь имя ascending) со значением по умолчанию False (булевое значение) и 
# сортировать продукты по количеству в порядке возрастания или убывания.
# Если в функцию не передан аргумент направления сортировки, сортировка должна проходить в порядке возрастания количества товаров 
# (от меньшего к большему). Если у продукта не указано количество, это не должно привести к ошибке, при получении значения по ключу, 
# если ключа в словаре нет - количество должно равняться 0 (используйте метод get())

def sort_products_by_quantity(list_product, ascending=False):
    print(len(list_product))
    if list_product[0]:
        for i in range(len(list_product)):
            if not list_product[i].get("quantity", False):
                item = list_product.pop(list_product[i])
        list_product.sort(key=lambda ist_product: ist_product["quantity"], reverse=ascending)
    return list_product


# Напишите функцию average_price_per_category(), которая принимает на вход список продуктов и возвращает новый словарь, 
# где ключи — категории, а значения — средняя цена продуктов в каждой категории. 
# Округлите результат вычисления до 1 знака после запятой. 
# Если у продукта отсутствует категория, это не должно привести к ошибке
def average_price_per_category(products):
    output_dict = {}
    for product in products:
        if product.get('category'):
            output_dict[product['category']] = 0
    for category in output_dict:
        count = 0
        for product in products:
            if product.get('category') and product['category'] == category:
                output_dict[category] += product['price']
            count += 1
        output_dict[category] = round(output_dict[category] / count, 1)
    return output_dict


# Напишите функцию group_products_by_category(products), которая принимает на вход список продуктов и 
# возвращает словарь, где ключи — категории, а значения — списки продуктов в каждой категории. 
# Если у продукта отсутствует категория, это не должно привести к ошибке. 
# Такой продукт игнорируется программой
def group_products_by_category(list_product):
    final_dict = {}
    if list_product != [{}]:
        for i in range(len(list_product)):
            time = list_product[i].get("category")
            final_dict[time] = []
            for count in range(len(list_product)):
                if time == list_product[count].get("category"):
                    final_dict[time].append(list_product[count])
    return final_dict

print(group_products_by_category(products))
