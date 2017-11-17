import sys
import csv
import curses
from random import randint
from timeit import default_timer

main_menu = '''---PLAY GAME---
---BEST PLAYERS---
---QUIT GAME---'''

submenu = '''---2 PLAYERS MODE---
---1 PLAYER VS COMPUTER---
---BACK---''' 

score_board = '''×××××××××××××××××××××××
××××× TOP PLAYERS ×××××
×××××××××××××××××××××××
----BACK----'''


def player_names():
    player_one_name = str(input('Enter the first players name: '))
    player_two_name = str(input('Enter the second players name: '))
    return player_one_name, player_two_name    
  
   
def print_board(board):
    i = 0
    while i < 3:
        print("\n", "_________________", "\n")
        print("|", end="")
        j = 0
        while j < 3:
            print(" ", board[3*i + j], "|".rjust(2), end="")
            j += 1 
        i += 1
    print("\n", "_________________", "\n")


def cooridante_input():
    in_list = False
    chk_list = list("123456789")
    while not in_list:
        coordinate = input("Please enter the coordinate you want to mark: ")   
        if coordinate in chk_list:
            in_list = True
        else:
            print("\033[1;31mWrong input, try again!\033[0;0m")
    index = int(coordinate) - 1
    return index   
            

def player_generator():
    temp = randint(0, 1)
    if temp == 0:
        player_one = '\033[1;31mX\033[0;0m'
        player_two = '\033[1;32mo\033[0;0m'
    else:
        player_one = '\033[1;32mo\033[0;0m'
        player_two = '\033[1;31mX\033[0;0m'
    return player_one, player_two


def chk_winning_conditions(player_names, reserve_list, player_generator, board, new_game):
    i = 0
    while i < 3:        
        if board[0+3*i] == board[1+3*i] and board[1+3*i] == board[2+3*i]:
            if board[1+3*i] == player_one_mark:
                print(player_one_name, "is the winner!")
                '''with open ('tictactoe_scores.txt', 'a') as f:
                    f.write(player_one_name)'''
            else:
                print(player_two_name, "is the winner! ")
                '''with open ('tictactoe_scores.txt', 'a') as f:
                    f.write(player_two_name)'''
            return True      
        i += 1 

    j = 0
    while j < 3:
        if board[0+j] == board[3+j] and board[3+j] == board[6+j]:
            if board[3+j] == player_one_mark:
                print(player_one_name, "is the winner!")
                with open ('tictactoe_scores.txt', 'a') as f:
                    f.write(player_one_name)
            else:
                print(player_two_name, "is the winner! ")
                with open ('tictactoe_scores.txt', 'a') as f:
                   f.write(player_two_name)
            return True
        j += 1  

    if board[0] == board[4] and board[4] == board[8]:
        if board[4] == player_one_mark:
            print(player_one_name, "is the winner!")
            with open ('tictactoe_scores.txt', 'a') as f:
                f.write(player_one_name)
        else:
            print(player_two_name, "is the winner! ")
            with open ('tictactoe_scores.txt', 'a') as f:
               f.write(player_two_name)
        return True

    elif board[2] == board[4] and board[4] == board[6]:
        if board[4] == player_one_mark:
            print(player_one_name, "is the winner!")
            with open ('tictactoe_scores.txt', 'a') as f:
               f.write(player_one_name)
        else:
            print(player_two_name, "is the winner! ")
            with open ('tictactoe_scores.txt', 'a') as f:
               f.write(player_two_name)
        return True

    elif len(reserve_list) == 9:
        print('This is a draw!')
        return True

    else:
        return False
                              
   
def ai_random_choose(reserve_list):
    running = True
    while running:
        temp = randint(0, 8)
        if temp not in reserve_list:
            print("The computer choosed: ", temp)
            running = False
            return temp


def best_score():
    print('×××××××××××××××××××××××')
    print('××××× \033[1;31mTOP PLAYERS\033[0;0m ×××××')
    print('×××××××××××××××××××××××')  
    with open ('tictactoe_scores.txt', 'r') as f:
        player_scores = f.readlines()
        print(player_scores)
    user_enter = input('\nPlease press B to back to main menu: ') 
    if user_enter.lower() == 'b':      
        game_main_menu()
    
    

def submenu_highscores():
    try:
        stdscr = curses.initscr()
        stdscr.clear()
        curses.cbreak()
        curses.noecho()
        stdscr.keypad(1)
        stdscr.addstr(0, 0, score_board)
        stdscr.move(3, 0)
        stdscr.refresh()
        i = 0
        j = 0
        c = stdscr.getch()
        if  c == curses.KEY_ENTER or c == 10 or c == 13:
            game_main_menu()
                    
        stdscr.refresh()

    finally:
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()


def submenu_playgame():
    try:
        stdscr = curses.initscr()
        stdscr.clear()
        curses.cbreak()
        curses.noecho()
        stdscr.keypad(1)
        stdscr.addstr(0, 0, submenu)
        stdscr.move(0, 0)
        stdscr.refresh()
        i = 0
        j = 0
        counter = 0
        while 1:
            c = stdscr.getch()
            if c == curses.KEY_DOWN:
                y, x = stdscr.getyx()
                maxy, maxx = stdscr.getmaxyx()
                stdscr.move((y+1) % 3, x)
                counter += 1
            if c == curses.KEY_UP:
                y, x = stdscr.getyx()
                maxy, maxx = stdscr.getmaxyx()
                stdscr.move((y-1) % 3, x)
                counter -= 1
        
            if counter == 0 and (c == curses.KEY_ENTER or c == 10 or c == 13):
                stdscr.clear()
                curses.nocbreak()
                stdscr.keypad(0)
                curses.echo()
                curses.endwin()
                new_game()
            elif counter == 1 and (c == curses.KEY_ENTER or c == 10 or c == 13):
                stdscr.clear()
                curses.nocbreak()
                stdscr.keypad(0)
                curses.echo()
                curses.endwin()
                computer_playing()
            elif counter == 2 and (c == curses.KEY_ENTER or c == 10 or c == 13):
                game_main_menu()
                    
            stdscr.refresh()

    finally:
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()


def game_main_menu():
    try:
        stdscr = curses.initscr()
        stdscr.clear()
        curses.cbreak()
        curses.noecho()
        stdscr.keypad(1)
        stdscr.addstr(0, 0, main_menu)
        stdscr.move(0, 0)
        stdscr.refresh()
        i = 0
        j = 0
        counter = 0
        while 1:
            c = stdscr.getch()
            if c == curses.KEY_DOWN:
                y, x = stdscr.getyx()
                maxy, maxx = stdscr.getmaxyx()
                stdscr.move((y+1) % 3, x)
                counter += 1
            if c == curses.KEY_UP:
                y, x = stdscr.getyx()
                maxy, maxx = stdscr.getmaxyx()
                stdscr.move((y-1) % 3, x)
                counter -= 1
        
            if counter == 0 and (c == curses.KEY_ENTER or c == 10 or c == 13):
                submenu_playgame()
            elif counter == 1 and (c == curses.KEY_ENTER or c == 10 or c == 13):
                stdscr.clear()
                curses.nocbreak()
                stdscr.keypad(0)
                curses.echo()
                curses.endwin()
                best_score()
            elif counter == 2 and (c == curses.KEY_ENTER or c == 10 or c == 13):
                sys.exit(0)
            
            stdscr.refresh()


    finally:
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()    

    





def new_game():   
    start = default_timer()   
    global player_one_name, player_two_name
    player_one_name, player_two_name = player_names()
    global player_one_mark, player_two_mark
    player_one_mark, player_two_mark = player_generator()
    board = list("123456789")
    reserve_list = []
    print("\nPlayer one is: ", player_one_name)        
    print("Player two is: ", player_two_name)
    print_board(board)
    i = 1
    is_game_ended = False
    move = 0
    while not is_game_ended:             
        if (i % 2) == 1:
            print(player_one_name,'s turn')
            move = cooridante_input()           
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_one_mark
            reserve_list.append(move)          
        elif (i % 2) == 0:
            print(player_two_name,'s turn')
            move = cooridante_input()
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_two_mark
            reserve_list.append(move)
        i += 1
        print_board(board)
        is_game_ended = chk_winning_conditions(player_names, reserve_list, player_generator, board, new_game) 
                                               
    duration = default_timer() - start
    duration = int(duration)
    print('\nYou played' ,duration, 'sec.')
    user_enter = input('\nPlease press B to back to main menu: ') 
    if user_enter.lower() == 'b':      
        game_main_menu()
    
def computer_playing():
    start = default_timer()
    global player_one_name, player_two_name
    player_one_name = player_names()
    player_two_name = "Computer"
    global player_one_mark, player_two_mark
    player_one_mark, player_two_mark = player_generator()
    board = list("123456789")
    reserve_list = []        
    print("\nPlayer one is: ", player_one_name)        
    print("\nPlayer two is: ", player_two_name)
    print_board(board)
    i = 1
    is_game_ended = False
    move = 0
    while not is_game_ended:
        if (i % 2) == 1:
            print(player_one_name,'s turn')
            move = cooridante_input()           
            while move in reserve_list:
                print("\n\033[1;31mThis field is already taken!\033[0;0m")
                move = cooridante_input()
            board[move] = player_one_mark
            reserve_list.append(move) 
            print("user reserve list", reserve_list)
        if (i % 2) == 0:
            print("Player computers turn")
            move = ai_random_choose(reserve_list)
            board[move] = player_two_mark
            reserve_list.append(move)
            print("comp reserve list", reserve_list)
        i += 1
        print_board(board)
        is_game_ended = chk_winning_conditions(player_names, reserve_list, player_generator, board, new_game)

    duration = default_timer() - start
    duration = int(duration)
    print('\nYou played' ,duration, 'sec')
    user_enter = input('\nPlease press B to back to main menu: ') 
    if user_enter.lower() == 'b':      
        game_main_menu()
    
                 
game_main_menu()
    




