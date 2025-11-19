"""Игра Калькулятор"""

import random


DESCRIPTION = "What is the result of the expression?"


def calculate(num1, num2, operator):
    """Вычисляет результат выражения"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        raise ValueError(f"Unknown operator: {operator}")


def generate_round():
    """Генерирует один раунд игры"""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operator} {num2}"
    correct_answer = calculate(num1, num2, operator)
    
    return question, str(correct_answer)


if __name__ == "__main__":
    # Для прямого запуска файла
    from VD_games.games.engine import run_game
    run_game(__import__('VD_games.games.calc', fromlist=['']))
