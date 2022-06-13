# TIC-TAC-TOE
Here's my first project using python language.

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)

The board should be printed out every time a player makes a move You should be able to accept input of the player position and then place a symbol on the board.

First off, make sure you understand the project scope. What needs to happen?

We need to print a board.

Take in player input.

Place their input on the board.

Check if the game is won,tied, lost, or ongoing.

Repeat c and d until the game has been won or tied.

Ask if players want to play again.

PROJECT HINTS:

1.Start by deciding how you will store the player's marker positions (Xs and Os). Let's choose a list, where each index corresponds with a number on a keypad, which in turn corresponds with a position on the 3 by 3 board.

2.Create a list called board which will keep track of the player markers.

3.The list should already be the same length as your intended board.

4.Create a function that will print a board. Not just the list, but an actual representation of a board! This can be done with multiple print statements within the function. Think about how you would take elements from the list and print them out into the board. (You can also clear output in jupyter notebook with clear_output() . You need to import this, so at the top of a cell copy and paste: from IPython.display import clear_output.

5.Write a function which takes an input marker string 'X' or "O' and a given number and stores it to a list at that appendix. You might have to look up how to take input in python! input() Play around with input() to make sure you understand it.

6.Write a function that takes in the board and a player marker and checks it theres a win or a tie. The checking for a win should be a series of a bunch checks, for example: (board[7] == board[8] == board[9] == marker)would check the first top row if they all match a player's marker. Check for a tie (this means nobody won and the board list is full!)

7.Now begin writing functions that begin game play. You'll need to write a function which starts combining and calling the different functions you've made within it. For example, a function which asks for a player's move, then updates the board,then checks for a win, then prints out the board.

8.How can you keep the game continually going? Maybe try using a while loop. Something like, while the board isn't full and nobody's won...

9.You might want to think about how to use boolean objects as markers of the game's status. Alright we should have enough now to begin piecing things together!

We'll go step by step to run this project.

Thankyou here's comes my first project.

Let's begin.
