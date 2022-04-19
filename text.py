# Suppose, you want a message to be sent after an interval of time automatically.
# then just run the following code:

import pyautogui
import time
while True:
    time.sleep(3)
    #time interval is 3 seconds
    
    pyautogui.typewrite('I am testing my code. Sorry for this btw!')
    #the message you want to be typed
    
    pyautogui.press('enter')
    #after a certain interval of time 'enter' key is pressed


# after running the code click anywhere (where you want to send the desired message) as soon as possible
# And the message will be sent automatically after the interval of time because after an interval of time 'enter' key is pressed.
