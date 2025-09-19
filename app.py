import random

def hangman_game():
    words = ['banana', 'apple', 'orange', 'grapes', 'melon']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    guessed_letters = set()
    tries = 6
    print('Welcome to Hangman!')
    
    while tries > 0 and '_' in guessed:
        print('\nWord: ' + ' '.join(guessed))
        print(f'Guessed letters: {", ".join(sorted(guessed_letters))}')
        print(f'Tries left: {tries}')
        guess = input('Guess a letter: ').lower()
        if not guess.isalpha() or len(guess) != 1:
            print('Invalid input. Please enter one letter.')
            continue
        if guess in guessed_letters:
            print('Already guessed. Try again.')
            continue
        guessed_letters.add(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print('Good job!')
        else:
            tries -= 1
            print('Incorrect!')
    if '_' not in guessed:
        print(f'\nCongratulations! You guessed the word: {word}')
    else:
        print(f'\nGame over. The word was: {word}')

hangman_game()