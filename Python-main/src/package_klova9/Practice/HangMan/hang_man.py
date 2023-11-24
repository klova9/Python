import random as ran
import json
import re

# WIP


def choose_word():
    with open('words.json') as f:
        all_words = json.load(f)
        fmt_words = re.search(r'\b\w+\b', all_words[ran.randint(0, len(all_words) - 1)])
        word = str(fmt_words[0])
        return word

'''
def computer_guess(): 
    common_letters = ['e', 't', 'o', 'a', 'i', 'n', 'n', 's'] * 80
    uncommon_letters =['b', 'c', 'd', 'f', 'g', 'j', 'k', 'm', 'p', 'u', 'v', 'w', 'x', 'y', 'z'] * 20
    letters = common_letters + uncommon_letters
    #shuffle(letters)
    letter_guess = ran.choice(letters) 
    return str(letter_guess[0])
'''

def check_letter():
    word = choose_word()
    hidden_word = list('_' * len(word))
    print(''.join(hidden_word), word)
    guess = str(input('Enter a guess: '))
    list_word = list(word)
    while '_' in hidden_word:
        if guess not in list_word:
            print('Guess again')
        for i, letter in enumerate(list_word):
            if letter != '_' and guess == letter:
                hidden_word[i] = letter
        print(''.join(hidden_word))
        return hidden_word

choose_word()
check_letter()