import platform
import os
import random
import re
from unicodedata import normalize

def clear_screen():
    os_system = platform.system()
    if os_system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def get_word() -> str:
    list_words = []
    with open('hangman_game_data.txt', 'r', encoding='utf-8') as f:
        list_words = f.read().splitlines()
        f.close()

    index = random.randint(0, len(list_words) - 1)
    return list_words[index]

def normalize_letter(letter: str) -> str:
    return normalize('NFC', re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize('NFD', letter), 0, re.I))

def validate_if_win(letters: list[dict]) -> bool:
    return not len(list(filter(lambda i: i['find'] == False, letters))) > 0

def validate_input(input: str) -> bool:
    return input.isalpha() and len(input) == 1

def find_word(game_word: str) -> bool:
    letters: list[dict] = [{'letter': normalize_letter(x), 'find': False} for x in game_word]
    attemps: int = 8
    win: bool = False
    while(attemps > 0 and not win):
        my_input: str = input('Ingresa una letra: ')
        if not validate_input(my_input):
            print('Por favor ingrese un valor válido')
            continue

        letter: str = normalize_letter(my_input)
        index: int = game_word.find(letter, 0)
        if index >= 0:
            new_letters = letters
            letters = list(map(lambda i: {'letter': i['letter'], 'find': True} if i['letter'] == letter else i, new_letters))
        else:
            attemps = attemps - 1

        if (attemps > 0):
            win = validate_if_win(letters)

    return win

def run():
    clear_screen()
    game_word: str = get_word()
    result: bool = find_word(game_word)
    if result:
        print('Ganaste')
    else:
        print('Perdiste')

if __name__ == '__main__':
    run()
