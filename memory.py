"""
Zachary Okayli Masaryk
Memory Board Game
12.13.2022
"""

import random
import numpy as np
import time

rows = 4
columns = 4

def visible_board(rows, columns):
    """
        creates a dictionary for the initial, untouched game board
        args:
            rows:
                the number of rows on the game board
            columns:
                the number of columns on the game board
        returns:
            key:
                a key displaying a chronological series of nummbers and their correlating definitions.
    """
    key = {}
    board_size = rows * columns
    for i in range(1, board_size + 1):
        key[i] = str(i)
    return key


def hidden_list(rows, columns):
    """
    indexes the English alphabet and creates a shuffled list containing a number of doubled letters that correlates with the memory game's
    board size
        args:
            rows: the number of rows on the game board
            
            columns: the number of columns on the game board
            
        returns:
            list: a list displaying a shuffled group of letters for a new game board
    """
    ALPHABET = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
    board_size = rows * columns
    over_slicing_addition = board_size - 52
    over_slicing_multiplier = board_size//52
    
    hidden_values = []
    for i in range(board_size):
        if board_size > 52:
            ALPHABET += ALPHABET[:over_slicing_addition]
        elif board_size > 104:
            ALPHABET = ALPHABET * over_slicing_multiplier
        hidden_values.append(ALPHABET[i])
        random.shuffle(hidden_values)
    return hidden_values
    
    
def hidden_board(rows, columns):
    """
    creates a dictionary containing the game boards hidden values (the letters)
        args:
            rows: the number of rows on the game board
            
            columns: the number of columns on the game board
            
        returns:
            key: a key displaying a chronological series of nummbers (representing the numbers on the game board) and their correlating letters.
    """    
    hidden = hidden_list(rows, columns)
    hidden_dictionary = {}
    for i in range(len(hidden)+1):
        if i > 0:
            hidden_dictionary[i] = hidden[i-1]
    return hidden_dictionary        
      

def memory_board(rows, columns, visible):
    """
    creates an array of letters out of the dictionary from visible().
        args:
            rows: the number of rows on the game board
            
            columns: the number of columns on the game board  
        returns:
            game board (dictionary/array)
    """ 
    for i in range(1, len(visible)+1):
        if i % columns == 0:
            print(visible[i], end = "\n")
        elif len(visible[i]) == 2:
            print(visible[i], end = ' ')
        elif len(visible[i]) == 1:
            print(visible[i], end = '  ') 
    

def blank_lines(rows, columns):
    """
    prints out a series of blank arrays in order to showcase the board being updated.
        args: 
            rows: the number of rows on the game board
            
            columns: the number of columns on the game board
            
        returns:
            blank game board
    """
    board_size = rows * columns
    for i in range(1,(board_size)*4):
        if i % columns == 0:
            print(" ", end = "\n")
        else: 
            print("  ", end = ' ')
    print("\n")


def checks(index1, index2, visible, hidden):
    """
    takes the user's two numeral guesses, and examines whether those two numbers already have matching letter values or not;
    makes sure that the user's numbers do not exceed the board size.
        Args:
            index1: user answer 1
            index2: user answer 2
            visible: the visible dictionary
            hidden: the hidden dictionary
        returns:
            False: if the conditionals are true, it returns false. This is a prerequiste for a conditional within my playgame function.
    """  
    for i in range(1, len(visible) + 1):
        if index1/len(visible) > 1.0 or index2/len(visible) > 1.0:
            return False
        elif visible[index1] == hidden[index1] or visible[index2] == hidden[index2]:
            return False
        
             
def has_won(rows, columns, hidden, time_elapsed, guesses):
    """
    winning statement for the game
            args: the parameters for memory_board()
            returns: the winning statement
    """   
    print("\n")
    print("You win!")
    memory_board(rows, columns, visible = hidden)
    print("It took you " + str(guesses) + " " + "guesses and " + str(time_elapsed) + " " + "seconds.")


def play_game():
    """
    Combines all functions into an interactive memory game. The user is prompted to keep trying to find matching letters. First, the program
    asks them to guess two numbers, and if the two numbers contain dictionary values (letters) that match, thoes values stay flipped over.
    The game ends once the entire board is flipped over. The user is then presented with a statement telling them how much time passed.
    """ 
    hidden = hidden_board(rows, columns)
    visible = visible_board(rows, columns)
    guess_two = "Guess two squares: "
    invalid = "Invalid number(s)"
    begin = time.time()
    
    #first board
    memory_board(rows, columns, visible)
    
    guesses = 0
    while hidden != visible:
        #user answer
        user_answer = (input(guess_two))
        a, b = user_answer.split()
        index1 = int(a)
        index2 = int(b)
        
        if checks(index1, index2, visible, hidden) == False:
            print(invalid)
            guesses += 1
            
        elif hidden[index1] == hidden[index2]:
            visible[index1] = hidden[index1]
            visible[index2] = hidden[index2]
            memory_board(rows, columns, visible)
            guesses += 1

        else:
            visible[index1] = hidden[index1]
            visible[index2] = hidden[index2]
            memory_board(rows, columns, visible)
            time.sleep(2)
            blank_lines(rows, columns)
            visible[index1] = str(index1)
            visible[index2] = str(index2)
            memory_board(rows, columns, visible)
            guesses += 1
            
        time_elapsed = int(time.time() - begin)
    has_won(rows, columns, hidden, time_elapsed, guesses)


if __name__ == "__main__":
    play_game()
