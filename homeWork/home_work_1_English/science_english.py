# Создание переменных
question_count = 0
question_reward = 10
count_true_questions = 0

# Блок вопросов
def Question_exists_is(name_in, count_in, true_count):
    word_in = input(f"Какое слово пропущено?\nMy name ___ {name_in}. \n")
    if word_in == "is":
        print("Ответ верный!\nВы получаете 10 баллов!")
        true_count += 1
    else:
        print(f"Неправильно.\nПравильный ответ: is")
    count_in += 1
    return count_in, true_count
        
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
        
def Status_count(count_question_in, count_true_questions_in, reward_in):
    print(f"Вы ответили на {count_true_questions_in} вопросов из {count_question_in} верно.")
    print(f"Вы заработали {count_question_in * reward_in} баллов.")
    
    
# end def
    
# Выполняем основной блок приветствия пользователю
name_user = input("Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут? \n")
print(f"Привет, {name_user}, начинаем тренировку!")

# Выполняем блок вопосов
Question_exists_is(name_user)
Question_exists_am()
Question_exists_in()

print(f"Вот и всё, {name_user}!")
Status_count(question_count, count_true_questions, question_reward)