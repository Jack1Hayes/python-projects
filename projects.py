# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:24:30 2022

@author: Hayes
"""
# madlib project

#youtuber = "jack"
#print(f"subscribe to {youtuber}")

#adj = input('adjective')
#verb1 = input('verb1')
#verb2 = input('verb2')
#famousperson = input ('famousperson')

#madlib = f'Computer programing is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famousperson}'
#print(madlib)

# guess the number

import random

#def guess(x):
#    random_number=random.randint(1, x)
#    guess = 0
#    while guess != random_number:
#        guess = int(input(f"guess a number between 1 and {x}:"))
#        print(guess)
#        if guess < random_number:
#            print ('too low')
#        elif guess > random_number:
#            print ('too high')
#    print('correct')

#guess(10)

#def computer_guess(x):
#    low = 1
#    high = x
#    feedback = ''
#    while feedback != 'c':
#        if low != high:
#            guess = random.randint(low, high)
#        else:
#            guess = low
#        feedback = input(f'is {guess} too high (h), or too low(l), or correct(c)')
#        if feedback == 'h':
#            high = guess - 1
#        if feedback == 'l':
#            low = guess +1
#    print(f'correct {guess}')
    
#computer_guess(10)

#rock paper scissors

#import random

#def play():
#    user = input ("'r' for rock, 's' for scissors, 'p' for paper:")
#    computer = random.choice(['r','p','s'])
    
#    if user == computer:
#        return 'tie'
#    if is_win(user, computer):
#        return 'win'
    
#    return 'you lost'

#def is_win(player, opponent):
#    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#        return True
    
#print(play())

#hangman
#import string

#word = input('choose a word:')

#def hangman():
#    word_letters = set(word)
#    alphabet = set(string.ascii_lowercase)
#    used_letters = set()
    
#    lives = 6
    
#    while len(word_letters) > 0 and lives > 0:
#        print('used letters: ', ' '.join(used_letters))
        
#        word_list = [letter if letter in used_letters else '-' for letter in word]
#        print('Current word: ', ' '.join(word_list))
#        print('you have', lives, 'lives left')
        
#        user_letter = input ('Guess a letter:').lower()
#        if user_letter in alphabet - used_letters:
#            used_letters.add(user_letter)
#            if used_letters in word_letters:
#                word_letters.remove(user_letter)
                
#            else: 
#                lives = lives - 1
#                print('letter not in the word')
#                
#        elif user_letter in used_letters:
#            print('guessed')
            
#        else:
#            print('invalid character')
#    if lives == 0:
#        print('sorry you did the word was', word)
#    else:
#        print('congratulations')


#print(hangman())

#tic-tac-toe


    
