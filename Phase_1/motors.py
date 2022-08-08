import sys, tty, termios
from gpiozero import Motor, PWMOutputDevice
from time import sleep

#motor pins -> led pins
motor_forward = [26,19]

motors = [
    Motor(motor_forward[0], motor_forward[1], pwm=False)
]

#get a character from the window
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
    return ch

#list to convert key ino motor on/off values -> direction

direction = {
    '1' : "forward",
    '5' : "stop",
    '0' : "reverse"
}

current_dir = "stop"

while True:

    if (current_dir == "forward"):
        motors[0].forward()
    elif (current_dir == "reverse"):
        motors[0].backward()
    else:
        motors[0].stop()

    #check for the next key press
    ch = getch()
    #p -> quit

    if(ch == 'p'):
        break

    elif(ch in direction.keys()):
        current_dir = direction[ch]
        print(current_dir)
