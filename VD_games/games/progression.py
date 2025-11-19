"""Игра Арифметическая прогрессия"""

import random


DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step, length):
    """Генерирует арифметическую прогрессию"""
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    return progression


def generate_round():
    """Генерирует один раунд игры"""
    length = random.randint(5, 10)  # Длина прогрессии от 5 до 10
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    hidden_index = random.randint(0, length - 1)
    
    progression = generate_progression(start, step, length)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    
    question = " ".join(progression)
    
    return question, correct_answer


if __name__ == "__main__":
    from VD_games.games.engine import run_game
    run_game(__import__('VD_games.games.progression', fromlist=['']))
