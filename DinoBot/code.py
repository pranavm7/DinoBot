"""
This is a prototype project developed by Pranav Mahajan.
Purpose of this bot is to play the dino easter egg in google chrome.
The screen res of my machine is 1366x768. Game will run offline on chrome.
Dimensions of game used are from: chrome:\\dino (It is maximized from mid to left)
You will have to adjust the globals "x_pad" & "y_pad" to adjust the program to your res
Have fun!
"""

#Co-ordinates to capture game-area only
x_pad = 30
y_pad = 196

#External libraries:-
#ImageGrab,ImageOps,win32api,win32con.
import os
import ImageGrab
import time
import ImageOps
import win32api
import win32con
from numpy import *

#This creates a screenshot and saves it in the current directory. I left it in here so that you (the end user),
#can easily adjust this to your resolution. PS:- uncomment the funciton call in main()!
'''
def screengrab():
    box =(x_pad+1,y_pad+1,x_pad+300,y_pad+162)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im
'''
#Created a function to greyscale the screenshot  [it is 2 pixels wide because faster processing,
#it isn't 1 because that gives a decimal value :) ]
#The commented command saves the screenshot before greyscale to pwd, for debugging purposes.
def grab():
    box =(x_pad+70,y_pad+150,x_pad+250,y_pad+151)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    b = array(im.getcolors())
    b = b.sum()
    print b
    return b

#Created a jump function  
def jump():
    win32api.keybd_event(win32con.VK_SPACE,0,0,0)
    #time.sleep(0.1)
    win32api.keybd_event(win32con.VK_SPACE,0,win32con.KEYEVENTF_KEYUP,0)
    
def main():
  
    while True:
        #screengrab()
        grab()
        J=grab()
        if J!=435:
            jump()
            print 'Jumped!'
        print 'success'
    #A simple if statement to make it do the thing! XD
    #The print statements are for debugging purposes, feel free to comment it out.
