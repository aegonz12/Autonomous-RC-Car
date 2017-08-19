import time
from Servo import Servo

servoPin = "P9_14"
dutyCycle = Servo.MIDDLE_DUTY_CYCLE

minDuty = Servo.MIN_DUTY_CYCLE
maxDuty = Servo.MAX_DUTY_CYCLE

servo = Servo()

servo.attach(servoPin, dutyCycle)
