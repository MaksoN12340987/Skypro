# Создаём переменные для работы программы
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
user_input_ready = None
number_of_correct_answers = 0



# Задаём блок начала
def checking_user_readiness():
    user_input = input('Привет! \nПредлагаю проверить свои знания английского! \nНаберите "ready", чтобы начать!\n')
    if user_input == "ready":
        return user_input
    else:
        print('Кажется, вы не хотите играть. Очень жаль.')

# Задаём блок вопросов
def checking_questions(questions_list, questions_answers):
    correct_answers = 0
    for i in range(len(questions_list)):
        if questions_answers[i] == input(f"{questions_list[i]}\n"):
            print('Ответ верный!')
            correct_answers += 1
        else:
            print(f"Неправильно. Правильный ответ: {questions_answers[i]}")
    return correct_answers

# Задаём блок итога
def status_of_answers(number_of_questions_user, correct_answers_user):
    fracton_true_question = (correct_answers_user / number_of_questions_user) * 100
    print(f"Вы ответили на {correct_answers_user} вопросов из {number_of_questions_user} верно. Это {round(fracton_true_question, 2)} процентов.")



# Выполняем основной блок кода
if len(questions) == len(answers) :
    if checking_user_readiness():
        number_of_correct_answers = checking_questions(questions, answers)
        status_of_answers(len(questions), number_of_correct_answers)
else:
    print("Количество вопросов и ответов различается")
