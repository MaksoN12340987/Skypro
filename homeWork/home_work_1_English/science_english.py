# Создание переменных
coll_question = 3
question_reward = 10
count_true_questions = 0

# Блок вопросов
def Question_exists_is(name_in):
    true_count = 0
    word_in = input(f"Какое слово пропущено?\nMy name ___ {name_in}. \n")
    if word_in == "is":
        print("Ответ верный!\nВы получаете 10 баллов! \n")
        true_count += 1
    else:
        print(f"Неправильно.\nПравильный ответ: is \n")
    return true_count
        
def Question_exists_am():
    true_count = 0
    word_in = input(f"Какое слово пропущено?\nI ___ a coder. \n")
    if word_in == "am":
        print("Ответ верный!\nВы получаете 10 баллов! \n")
        true_count += 1
    else:
        print(f"Неправильно.\nПравильный ответ: am \n")
    return true_count
        
def Question_exists_in():
    true_count = 0
    word_in = input(f"Какое слово пропущено?\nI live ___ Moscow. \n")
    if word_in == "in":
        print("Ответ верный!\nВы получаете 10 баллов! \n")
        true_count += 1
    else:
        print(f"Неправильно.\nПравильный ответ: in \n")
    return true_count
        
def Status_count(coll_question_in, count_true_questions_in, reward_in):
    print(f"Вы ответили на {count_true_questions_in} вопросов из {coll_question_in} верно.")
    print(f"Вы заработали {count_true_questions_in * reward_in} баллов.")
    fracton_true_question = (count_true_questions_in / coll_question_in) * 100
    print(f"Это {round(fracton_true_question, 2)} процентов.")

    
# Выполняем основной блок приветствия пользователю
name_user = input("Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут? \n")
print(f"Привет, {name_user}, начинаем тренировку! \n")

# Выполняем блок вопосов
count_true_questions += Question_exists_is(name_user)
count_true_questions += Question_exists_am()
count_true_questions += Question_exists_in()

print(f"Вот и всё, {name_user}!")
Status_count(coll_question, count_true_questions, question_reward)
