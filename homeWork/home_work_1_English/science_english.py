# Создание переменных
question_count = 0

# Блок вопросов
def Question_exists_is(name_in):
    word_in = input(f"Какое слово пропущено?\nMy name ___ {name_in}")
    if word_in == "is":
        print("Ответ верный!\nВы получаете 10 баллов!")
    else:
        print(f"Неправильно.\nПравильный ответ: is")
    
# Вывод приветствия пользователю
name_user = ans = input("Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут? ")
print(f"Привет, {name_user}, начинаем тренировку!")

# Выполняем программу
Question_exists_is(name_user)