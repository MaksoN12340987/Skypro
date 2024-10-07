# Создание переменных
number_of_questions = 3
reward_for_answer = 10
number_of_correct_answers = 0

# Блок вопросов
def question_missed_is(name_in):
    correct_answers = 0
    user_word = input(f"Какое слово пропущено?\nMy name ___ {name_in}. \n")
    if user_word == "is":
        print("Ответ верный!\nВы получаете 10 баллов! \n")
        correct_answers += 1
    else:
        print(f"Неправильно.\nПравильный ответ: is \n")
    return correct_answers
        
def question_missed_am():
    correct_answers = 0
    user_word = input(f"Какое слово пропущено?\nI ___ a coder. \n")
    if user_word == "am":
        print("Ответ верный!\nВы получаете 10 баллов! \n")
        correct_answers += 1
    else:
        print(f"Неправильно.\nПравильный ответ: am \n")
    return correct_answers
        
def question_missed_in():
    correct_answers = 0
    user_word = input(f"Какое слово пропущено?\nI live ___ Moscow. \n")
    if user_word == "in":
        print("Ответ верный!\nВы получаете 10 баллов! \n")
        correct_answers += 1
    else:
        print(f"Неправильно.\nПравильный ответ: in \n")
    return correct_answers
        
def status_of_answers(number_of_questions_user, correct_answers_user, reward_for_answer_user):
    print(f"Вы ответили на {correct_answers_user} вопросов из {number_of_questions_user} верно.")
    print(f"Вы заработали {correct_answers_user * reward_for_answer_user} баллов.")
    
    fracton_true_question = (correct_answers_user / number_of_questions_user) * 100
    print(f"Это {round(fracton_true_question, 2)} процентов.")

    
# Выполняем основной блок, приветствиe пользователю
name_user = input("Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут? \n")
print(f"Привет, {name_user}, начинаем тренировку! \n")

# Выполняем блок вопpосов
number_of_correct_answers += question_missed_is(name_user)
number_of_correct_answers += question_missed_am()
number_of_correct_answers += question_missed_in()

print(f"Вот и всё, {name_user}!")
status_of_answers(number_of_questions, number_of_correct_answers, reward_for_answer)
