import random as ran
import json
import regex as re
import keyboard

# WIP

# This code defines a function called choose_word that selects a random word from a JSON file called 'words.json'. The selected word is then formatted using a regular expression to remove any non-word characters. The formatted word is returned as the result of the function.
def choose_word():
    with open('words.json') as f:
        all_words = json.load(f)
        fmt_words = re.search(r'\b\w+\b', all_words[ran.randint(0, len(all_words) - 1)])
        word = str(fmt_words[0])
        return word
# This code defines a function called computer_guess that generates a random letter. The function creates two lists, common_letters and uncommon_letters, which contain letters repeated a certain number of times. These lists are then concatenated into a new list called letters. Finally, a random letter is chosen from letters and returned as a string.
'''
def computer_guess(): 
    common_letters = ['e', 't', 'o', 'a', 'i', 'n', 'n', 's'] * 80
    uncommon_letters =['b', 'c', 'd', 'f', 'g', 'j', 'k', 'm', 'p', 'u', 'v', 'w', 'x', 'y', 'z'] * 20
    letters = common_letters + uncommon_letters
    #shuffle(letters)
    letter_guess = ran.choice(letters) 
    return str(letter_guess[0])
'''
# This code defines a function called check_letter() that prompts the user to enter a guess for a word. It then checks if the guess matches any letters in the word, updates a hidden word with the correct guesses, and returns the hidden word.
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