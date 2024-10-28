import math
import xbox
import RPi.GPIO as GPIO

GPIO_WHEEL_FL_FORWARD = 2
GPIO_WHEEL_FR_FORWARD = 3
GPIO_WHEEL_BL_FORWARD = 4
GPIO_WHEEL_BR_FORWARD = 17
GPIO_WHEEL_FL_BACK = 27
GPIO_WHEEL_FR_BACK = 22
GPIO_WHEEL_BL_BACK = 10
GPIO_WHEEL_BR_BACK = 9

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(GPIO_WHEEL_FL_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_WHEEL_FR_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_WHEEL_BR_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_WHEEL_BL_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_WHEEL_FL_BACK, GPIO.OUT)
GPIO.setup(GPIO_WHEEL_FR_BACK, GPIO.OUT)
GPIO.setup(GPIO_WHEEL_BR_BACK, GPIO.OUT)
GPIO.setup(GPIO_WHEEL_BL_BACK, GPIO.OUT)

def updateDirection(speed, angle):
    if speed == 0:
        GPIO_WHEEL_FL_FORWARD, GPIO_WHEEL_FR_FORWARD, GPIO_WHEEL_BL_FORWARD, GPIO_WHEEL_BR_FORWARD = GPIO.LOW
        GPIO_WHEEL_FL_BACK, GPIO_WHEEL_FR_BACK, GPIO_WHEEL_BL_BACK, GPIO_WHEEL_BR_BACK = GPIO.LOW
    else:
        if angle == 0:
            if speed > 0:
                GPIO_WHEEL_FL_FORWARD, GPIO_WHEEL_FR_FORWARD, GPIO_WHEEL_BL_FORWARD, GPIO_WHEEL_BR_FORWARD = GPIO.HIGH
                GPIO_WHEEL_FL_BACK, GPIO_WHEEL_FR_BACK, GPIO_WHEEL_BL_BACK, GPIO_WHEEL_BR_BACK = GPIO.LOW
            elif speed < 0:
                GPIO_WHEEL_FL_FORWARD, GPIO_WHEEL_FR_FORWARD, GPIO_WHEEL_BL_FORWARD, GPIO_WHEEL_BR_FORWARD = GPIO.LOW
                GPIO_WHEEL_FL_BACK, GPIO_WHEEL_FR_BACK, GPIO_WHEEL_BL_BACK, GPIO_WHEEL_BR_BACK = GPIO.HIGH
        else:
            if angle > 0:
                GPIO_WHEEL_FL_FORWARD, GPIO_WHEEL_BL_FORWARD, GPIO_WHEEL_FR_BACK, GPIO_WHEEL_BR_BACK = GPIO.HIGH
                GPIO_WHEEL_FR_FORWARD, GPIO_WHEEL_BR_FORWARD, GPIO_WHEEL_FL_BACK, GPIO_WHEEL_BL_BACK = GPIO.LOW
            elif angle < 0:
                GPIO_WHEEL_FL_FORWARD, GPIO_WHEEL_BL_FORWARD, GPIO_WHEEL_FR_BACK, GPIO_WHEEL_BR_BACK = GPIO.LOW
                GPIO_WHEEL_FR_FORWARD, GPIO_WHEEL_BR_FORWARD, GPIO_WHEEL_FL_BACK, GPIO_WHEEL_BL_BACK = GPIO.HIGH

if __name__ == '__main__':
    joy = xbox.Joystick()

    while not joy.Back():

         # motors
        _, speed = joy.leftStick()
        angle, _ = joy.rightStick()

        updateDirection(speed, angle)

    joy.close()
