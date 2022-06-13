#!/usr/bin/env python
# coding: utf-8

# Here's my first project using python language.
# 
# Here are the requirements:
# 
# 2 players should be able to play the game (both sitting at the same computer)
# 
# The board should be printed out every time a player makes a move You should be able to accept input of the player position and then place a symbol on the board.
# 
# First off, make sure you understand the project scope. What needs to happen?
# 
# We need to print a board.
# 
# Take in player input.
# 
# Place their input on the board.
# 
# Check if the game is won,tied, lost, or ongoing.
# 
# Repeat c and d until the game has been won or tied.
# 
# Ask if players want to play again.
# 
# PROJECT HINTS:
# 
# 1.Start by deciding how you will store the player's marker positions (Xs and Os). Let's choose a list, where each index corresponds with a number on a keypad, which in turn corresponds with a position on the 3 by 3 board.
# 
# 2.Create a list called board which will keep track of the player markers.
# 
# 3.The list should already be the same length as your intended board.
# 
# 4.Create a function that will print a board. Not just the list, but an actual representation of a board! This can be done with multiple print statements within the function. Think about how you would take elements from the list and print them out into the board. (You can also clear output in jupyter notebook with clear_output() . You need to import this, so at the top of a cell copy and paste: from IPython.display import clear_output.
# 
# 5.Write a function which takes an input marker string 'X' or "O' and a given number and stores it to a list at that appendix. You might have to look up how to take input in python! input() Play around with input() to make sure you understand it.
# 
# 6.Write a function that takes in the board and a player marker and checks it theres a win or a tie. The checking for a win should be a series of a bunch checks, for example: (board[7] == board[8] == board[9] == marker)would check the first top row if they all match a player's marker. Check for a tie (this means nobody won and the board list is full!)
# 
# 7.Now begin writing functions that begin game play. You'll need to write a function which starts combining and calling the different functions you've made within it. For example, a function which asks for a player's move, then updates the board,then checks for a win, then prints out the board.
# 
# 8.How can you keep the game continually going? Maybe try using a while loop. Something like, while the board isn't full and nobody's won...
# 
# 9.You might want to think about how to use boolean objects as markers of the game's status. Alright we should have enough now to begin piecing things together!
# 
# We'll go step by step to run this project.
# 
# Thankyou here's comes my first project.
# 
# Let's begin.

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
# 

# In[2]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


# TEST Step 1: run your function on a test version of the board list, and make adjustments as necessary
# 

# In[4]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
# 

# In[5]:


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ')

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# TEST Step 2: run the function to make sure it returns the desired output
# 

# In[ ]:


player_input()


# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
# 

# In[6]:


def place_marker(board, marker, position):
    board[position] = marker


# TEST Step 3: run the place marker function using test parameters and display the modified board
# 

# In[17]:


place_marker(test_board,'$',8)
display_board(test_board)


# Step 4: Write a function that takes in a board and checks to see if someone has won.
# 

# In[7]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# TEST Step 4: run the win_check function against our test_board - it should return True
# 

# In[20]:


win_check(test_board,'X')


# In[8]:


 
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
# 

# In[9]:


def space_check(board, position):
    
    return board[position] == ' '


# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
# 

# In[10]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use.
# 

# In[12]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
# 

# In[13]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ')


# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
# 

# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! player 1 have won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game have been drawn!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# 
