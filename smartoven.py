import time, sys
from fhict_cb_01.CustomPymata4 import CustomPymata4
from pymata4 import pymata4

BUTTON1 = 8
t = 15
level = 0
prevLevel = 0
greenLed = 5
redLed = 4
buzzer = 3

def ButtonChanged(data):
    global level
    level = data[2] # get the level
    

def timer(t):
    while t:
        board.displayShow(t)
        board.digital_write(redLed, 1)
        board.digital_write(greenLed, 0)
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        board.displayShow(t)

    print("message send")  
    print("pizza is ready!")
    melody()
    board.digital_write(redLed, 0)
    board.displayShow("0000")
    board.digital_write(greenLed, 1)

def melody():
    board.pwm_write(3, 660)
    time.sleep(0.1)
    board.pwm_write(3, 0)

    time.sleep(0.15)

    board.pwm_write(3, 660)
    time.sleep(0.1)
    board.pwm_write(3, 0)

    time.sleep(0.15)

    board.pwm_write(3, 660)
    time.sleep(0.1)
    board.pwm_write(3, 0)

    time.sleep(0.15)
   

def setup():
    global board
    board = CustomPymata4(com_port = "COM3")
    board.set_pin_mode_digital_input_pullup(BUTTON1, callback = ButtonChanged)
    board.set_pin_mode_digital_output(greenLed)
    board.set_pin_mode_digital_output(redLed)
    board.set_pin_mode_pwm_output(3)
    
def loop():
    global prevLevel
    if (prevLevel != level):
        # Lets respond on button level change.q
        prevLevel = level
    

setup()
while True:
    try:
        loop()
        if level == 0:
            timer(int(t))
    except KeyboardInterrupt: # crtl+C
        print ('shutdown')
        board.shutdown()
        sys.exit(0)  