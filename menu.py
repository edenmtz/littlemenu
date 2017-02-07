#!/usr/bin/env python

import curses

screen = curses.initscr()

curses.start_color()
curses.noecho()
curses.cbreak()
screen.keypad(True)

options = ["altas", "bajas", "cambios","mas","menos","menos","dos","tres","cuatro","cinco"]
positions = [0 for item in options]
positions[0]=1


def drawMenu (options, positions):
    n = 0
    choice = -1
    hrz=1
    format=curses.A_NORMAL
    for option in options:
        if positions[n] == 1:
            format = curses.A_REVERSE
            choice = n
        screen.addstr(1,hrz,option,format)
        hrz+=len(option)+1
        format = curses.A_NORMAL
        n+=1
    return choice

temp = -1
key_press = ""



while (key_press != ord("q")):       

    if key_press == curses.KEY_UP:
        if temp == 0:
            positions[len(positions)-1] = 1
            positions[temp]=0            
        else:
            positions[temp-1]=1
            positions[temp]=0
            
    elif key_press == curses.KEY_DOWN:
        if temp == len(positions)-1:
            positions[0] = 1
            positions[temp]=0
        else:
            positions[temp+1]=1
            positions[temp]=0
    
    screen.addstr(20,1,"key_press: "+str(key_press),curses.A_NORMAL)    

#    screen.addstr(23,15,"positions[1]:" +str(positions[1]),curses.A_NORMAL)
#    screen.addstr(24,15,"positions[2]:" +str(positions[2]),curses.A_NORMAL)
    temp = drawMenu(options, positions)
    screen.refresh()
    key_press = screen.getch()
    

curses.endwin()
