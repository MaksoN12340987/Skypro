# Создание переменных
question_count = 0

# Блок вопросов
def Question_exists_is(name_in):
    word_in = input(f"Какое слово пропущено?\nMy name ___ {name_in}. \n")
    if word_in == "is":
        print("Ответ верный!\nВы получаете 10 баллов!")
    else:
        print(f"Неправильно.\nПравильный ответ: is")
        
def Question_exists_am():
    word_in = input(f"Какое слово пропущено?\nI ___ a coder. \n")
    if word_in == "am":
        print("Ответ верный!\nВы получаете 10 баллов! \n")
    else:
        print(f"Неправильно.\nПравильный ответ: am")
        
def Question_exists_in():
    word_in = input(f"Какое слово пропущено?\nI live ___ Moscow. \n")
    if word_in == "in":
        print("Ответ верный!\nВы получаете 10 баллов!")
    else:
        print(f"Неправильно.\nПравильный ответ: in")
    
# Выполняем основной блок приветствия пользователю
name_user = ans = input("Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут? \n")
print(f"Привет, {name_user}, начинаем тренировку!")

# Выполняем блок вопосов
Question_exists_is(name_user)
Question_exists_am()
Question_exists_in()
