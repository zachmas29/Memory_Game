Description:

*This is a memory-matching game that uses two dictionaries to create a board: 
one that’s visible to the player and one that holds the hidden letter values. 
At the start of the game, the player sees a grid of numbered tiles. Behind each number is a letter, 
and each letter appears exactly twice somewhere on the board.
*The player is asked to guess two numbers at a time. If the letters behind those numbers match, 
they stay flipped. If not, they flip back over after a short pause. The goal is to keep guessing 
until all the letters have been revealed.

*Behind the scenes, the game swaps between the visible and hidden values depending 
on whether the player guesses correctly. One of the cool features is that the board is 
flexible — you can change the number of rows and columns, and the game will generate a 
matching set of letter pairs to fill it. That part happens in the hidden_list() function, 
which builds the letter set based on the size of the board.
