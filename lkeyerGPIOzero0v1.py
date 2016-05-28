#This program will use the gpiozero library to register button presses
from gpiozero import Button
from signal import pause
from time import sleep

#P,R,M,I N,C,F
buttonPins = [ 6,13,16,20,19,26,21]

buttons = [Button(pin) for pin in buttonPins]
#P,R,M,I N,C,F
buttonState = [0,0,0,0,0,0,0]



##########DEBUG STUFF#################
DEBUG = true
def debug(text):
    if DEBUG:
        print(text)
##########DEBUG STUFF#################

def wasReleased(the_button):
    "this function is called when a button is released
    it first sends the states to be proccessed, then 
    removes the pin it is passed bi finding the pin from the
    buttoPins list and seting it to 0"

    debug("Released:"),
    debug(the_button.pin.number)
    
    processCommand()
    buttonState[ buttonPins.index(the_button.pin.number) ] = 0
    
def wasPressed(the_button):
    "This function is called when a button is pressed,
     it sets that button to 1 in the buttonState list"
    debug("Pressed: "),
    debug(the_button.pin.number)
    buttonState[ buttonPins.index(the_button.pin.number) ] = 1


def main():
    for button in buttons:
        button.when_pressed = wasPressed
        button.when_released = wasReleased

    while True:
        #print("main"),
        #print(buttonState)
        sleep(.7)
    pause()






def processCommand():
    "This will eventually handle looking up which char 
    to send and send it to another process to send either bluetooth or"

    debug("in process Command: "),
    debug(buttonState)
    debug("in procces still")
    sleep(2)
    debug("waking up")


def pinkyPressed():
    buttonState[0] = 1
    
def pinkyReleased():
    #send results, then,
    processCommand()
    buttonState[0] = 0




if __name__ == "__main__":
    main()
