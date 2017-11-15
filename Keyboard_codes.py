
import curses

main_menu = '''---PLAY GAME---
---BEST PLAYERS---
---QUIT GAME---'''

try:
    stdscr = curses.initscr()
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
        
        if counter == 0 and c == curses.KEY_ENTER or c == 10 or c == 13:
            print('First')
        elif counter == 1 and c == curses.KEY_ENTER or c == 10 or c == 13:
            print('Second option')
        elif counter == 2 and c == curses.KEY_ENTER or c == 10 or c == 13:
            exit(0)
            
        stdscr.refresh()


finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()