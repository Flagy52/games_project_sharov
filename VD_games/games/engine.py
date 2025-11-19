"""Движок для запуска игр"""

import prompt


def run_game(game_module):
    """
    Запускает игру с заданным модулем
    """
    print("Welcome to the VD Games!")
    print()
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print()
    
    # Получаем описание игры из модуля
    print(game_module.DESCRIPTION)
    print()
    
    # Количество раундов
    rounds_count = 3
    
    for _ in range(rounds_count):
        # Получаем вопрос и правильный ответ от игры
        question, correct_answer = game_module.generate_round()
        
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
