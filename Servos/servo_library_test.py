import time
from Servo import Servo



servoPin = "P9_14"
dutyCycle = Servo.MIN_DUTY_CYCLE
increment = 0.1



servo = Servo()
servo.attach(servoPin)
servo.setDutyCycle(dutyCycle)

time.sleep(1)

print servo.getPinStatus(), "\n"

time.sleep(1)



finished = False

while not finished:
	if dutyCycle + increment <= Servo.MAX_DUTY_CYCLE:
		dutyCycle = dutyCycle + increment
		servo.setDutyCycle(dutyCycle)
		print "DUTY CYCLE:", dutyCycle
	else:
		finished = True
		print "Finished first sweep"

	time.sleep(0.15)



finished = False



while not finished:
	if dutyCycle - increment >= Servo.MIN_DUTY_CYCLE:
		dutyCycle = dutyCycle - increment
		servo.setDutyCycle(dutyCycle)
		print "DUTY CYCLE:", dutyCycle
	else:
		finished = True
		print "Finished second sweep"

	time.sleep(0.15)



servo.detach()