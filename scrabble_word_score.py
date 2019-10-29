'''
Habitica Challenge October 2019

Challenge Description
In the game Scrabble each letter has a value. One completed word gives you a score.

Write a program that takes a word as an imput and outputs the calculated scrabble score.

Values and Letters:
1 - A, E, I, O, U, L, N, R, S, T
2 - D, G
3 - B, C, M, P
4 - F, H, V, W, Y
5 - K
8 - J, X
10 - Q, Z

Example:
The word "cabbage" gives you a score of 14 (c-3, a-1, b-3, b-3, a-1, g-2, e-1)

Extensions:
You can play a double or triple letter
You can play a double or triple word
'''

import os

let_val = {
    'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'R':1, 'S':1, 'T':1,
    'D':2, 'G':2,
    'B':3, 'C':3, 'M':3, 'P':3,
    'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
    'K':5,
    'J':8, 'X':8,
    'Q':10, 'Z':10
}

def select_action():
    print('Please Select Action:')
    op = -1
    while not(op == '1' or op == '0'):
        print(' 1 - Check word')
        print(' 0 - Exit')
        op = input('Option: ')
    return op

def check_valid_word(word):
    with open('sowpods.txt') as f:
        if word in f.read():
            return True
        return False

def enter_word():
    word = input('Please enter word: ').upper().strip()
    while not check_valid_word(word):
        word = input('Invalid Scrabble word. Please Try again: ').upper().strip()
    
    score = 0
    for let in word:
        score += let_val[let]
    print('Valid Scrabble word! The score for {} is: {}\n'.format(word, score))


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    print('Welcome to scrabble word value calculator!')
    opt = select_action()
    while opt != '0':
        enter_word()
        opt = select_action()

    print('Thanks for playing!')

main()