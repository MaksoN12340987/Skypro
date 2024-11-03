# Variables
words_low = dict(family="семья", hand= "рука", people="люди", 
                    evening= "вечер",minute="минута")

words_medium = dict(believe="верить", feel="чувствовать", make="делать", 
                    open="открывать", think="думать")

words_high = {"rural":"деревенский", "fortune":"удача", "exercise":"упражнение", 
                "suggest":"предлагать", "except":"кроме"}

difficulty = {"low":"легкий", "medium":"средний", "high":"сложный"}
levels = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}

# Принимает словарь с уровнем сложности и три словаря: лёгкий, средний, сложный
def choose_difficulty(dif_lvl, low_words, medium_words, high_words):
    print("Выберите уровень сложности.")
    keys_dif = list(dif_lvl.keys())
    for i in range(len(keys_dif)):
        if i != len(keys_dif)-1:
            print(dif_lvl[keys_dif[i]], end=", ")
        else:
            print(dif_lvl[keys_dif[i]], end=": \n")
    
    words = {}
    user_input = input().lower()
    if user_input == dif_lvl[keys_dif[0]]:
        words =  low_words
    elif user_input == dif_lvl[keys_dif[1]]:
        words =  medium_words
    elif user_input == dif_lvl[keys_dif[2]]:
        words = high_words
    else:
        words =  medium_words

    return words

# Принимает словарь с данными типа 'слово:перевод'
def play_game(dict_input):
    print("\nВыбран уровень сложности. Мы предложим 5 слов, подберите перевод.")
    asnwers = {}

    keys_dict = list(dict_input.keys())
    for i in range(len(keys_dict)):
        variable_str = str(dict_input[keys_dict[i]])
        variable_time = input(f"{keys_dict[i]}, {len(keys_dict[i])} букв, начинается на {variable_str[0]} \n")

        if variable_time == dict_input[keys_dict[i]]:
            print(f"Верно. {keys_dict[i]} — это {dict_input[keys_dict[i]]}. \n")
            asnwers[dict_input[keys_dict[i]]] = True
        else:
            print(f"Неверно. {keys_dict[i]} — это {dict_input[keys_dict[i]]}. \n")
            asnwers[dict_input[keys_dict[i]]] = False
    return asnwers

# Принимает словарь результатов со значениями: 'question:bool', словарь типа: 'слово:перевод'
def display_results(asnwers_result):
    print("\nПравильно отвечены слова:")

    keys_result = list(asnwers_result.keys())
    for i in range(len(keys_result)):
        if asnwers_result[keys_result[i]]:
            print(keys_result[i])
        else:
            continue
    
    print("\nНеправильно отвечены слова:")
    for i in range(len(keys_result)):
        if asnwers_result[keys_result[i]]:
            continue
        else:
            print(keys_result[i])

# Принимает словарь результатов со значениями: 'question:bool', словарь типа: 'level:ответ'
def calculate_rank(input_result, input_lvl):
    print("\nВаш ранг:")
    count = 0
    check = list(input_result.keys())
    for i in range(len(check)):
        if input_result[check[i]]:
            count += 1
        else:
            continue
    print(input_lvl[count])


# Выполняем программу
guess_words = choose_difficulty(difficulty, words_low, words_medium, words_high)
user_asnwers = play_game(guess_words)
display_results(user_asnwers)
calculate_rank(user_asnwers, levels)
