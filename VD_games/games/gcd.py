"""Игра Наибольший общий делитель"""

import random
import math


DESCRIPTION = "Find the greatest common divisor of given numbers."


def find_gcd(a, b):
    """Находит наибольший общий делитель двух чисел"""
    return math.gcd(a, b)


def generate_round():
    """Генерирует один раунд игры"""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    question = f"{num1} {num2}"
    correct_answer = find_gcd(num1, num2)
    
    return question, str(correct_answer)


if __name__ == "__main__":
    # Для прямого запуска файла
    from VD_games.games.engine import run_game
    run_game(__import__('VD_games.games.gcd', fromlist=['']))
