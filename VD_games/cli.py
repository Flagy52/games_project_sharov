import prompt

def welcome_user():
    """
    Приветствует пользователя в игре, спрашивает его имя и прощается.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
