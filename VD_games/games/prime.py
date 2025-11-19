"""Игра Простое ли число?"""

import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Проверяет, является ли число простым"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    """Генерирует один раунд игры"""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    
    return question, correct_answer


if __name__ == "__main__":
    from VD_games.games.engine import run_game
    run_game(__import__('VD_games.games.prime', fromlist=['']))
