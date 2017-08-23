import time
from Servo import Servo



servoPin = "P9_14"
dutyCycle = Servo.MIN_DUTY_CYCLE
increment = 0.1



servo = Servo()
servo.attach(servoPin, dutyCycle)
servo.setDutyCycle(dutyCycle)

time.sleep(1)

print servo.getPinStatus(), "\n"



while dutyCycle < Servo.MAX_DUTY_CYCLE:
	dutyCycle = dutyCycle + increment
	servo.setDutyCycle(dutyCycle)

	time.sleep(0.15)
	print "DUTY CYCLE: ", servo.getDutyCycle()


time.sleep(1)


while dutyCycle > Servo.MIN_DUTY_CYCLE:
	dutyCycle = dutyCycle - increment
	servo.setDutyCycle(dutyCycle)

	time.sleep(0.15)
	print "DUTY CYCLE: ", servo.getDutyCycle()



servo.detach()