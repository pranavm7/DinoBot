"""
This is a prototype project developed by Pranav Mahajan.
Purpose of this bot is to play the dino easter egg in google chrome.
Dimensions of game used are from: http://www.trex-game.skipser.com/
"""

#Globals
#---------------

x_pad = 378
y_pad = 228




import os
import ImageGrab
import time

def screengrab():
    box =(x_pad+1,y_pad+1,x_pad+607,y_pad+197)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screengrab()
    if __name__ == '__main__':
        main()    
