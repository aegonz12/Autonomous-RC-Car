import Adafruit_BBIO.PWM as PWM


"""
A class for controlling servos on the Beaglebone Black's PWM pins using the Adafruit BBIO library

The class is to be an interface for interacting between the Adafruit BBIO library specifically for servo control via PWM.
"""
class Servo:
	MIN_DUTY_CYCLE = 3
	MAX_DUTY_CYCLE = 14.5
	MIDDLE_DUTY_CYCLE = (MAX_DUTY_CYCLE + MIN_DUTY_CYCLE) / 2

	ALLOWED_PINS = ("P8_13", "P8_19", "P9_14", "P9_16", "P9_21", "P9_22")
	PINS_IN_USE = {"P8_13": False, "P8_19": False, "P9_14": False, "P9_16": False, "P9_21": False, "P9_22": False}



	# Object constructor
	def __init__(self):
		self.pin = None
		self.currentDuty = Servo.MIDDLE_DUTY_CYCLE
		self.frequency = None
		self.polarity = None



	# After an object is created it must be attached (associated) to a pin.
	# The pin must be a PWM pin, which are listed in the ALLOWED_PINS tuple
	# The pin must not already be attached
	# pin = PWM pin to be attached to the object
	# frequency = frequency to run the PWm pin at
	# polairty = polarity to run the PWM pin at
	def attach(self, pin, frequency = 60, polarity = 0):
		if pin not in Servo.ALLOWED_PINS:
			raise Exception(pin, " is not allowed.")
		elif Servo.PINS_IN_USE[pin] == True:
			raise Exception(pin, " is already in use.")
		else:
			self.pin = pin
			self.frequency = frequency
			self.polarity = polarity
			Servo.PINS_IN_USE[self.pin] = True
			PWM.start(pin, self.currentDuty, frequency, polarity)



	# When finished with a servo object, detach (unassociate) is from the pin
	# This allows the pin to be used later cleans up the pin
	def detach(self):
		if Servo.PINS_IN_USE[self.pin] == False:
			raise Exception(pin, " is not in use.")
		else:
			PWM.stop(self.pin)
			PWM.cleanup()
			Servo.PINS_IN_USE[self.pin] = False
			self.pin = None



	# Change the desired duty cycle
	# The new duty cycle must be within the upper and lower bounds of 3 and 14.5, respectivly
	def setDutyCycle(self, newDuty):
		if self.pin == None:
			raise Exception("No attached pin")
		elif (newDuty < Servo.MIN_DUTY_CYCLE) or (newDuty > Servo.MAX_DUTY_CYCLE):
			raise Exception("New duty cycle value out of bounds")
		else:
			self.currentDuty = newDuty
			PWM.setDutyCycle(self.pin, newDuty)



	# Returns a servo objects attached pin
	def getPin(self):
		return self.pin


	# Returns a servo objects current duty cycle
	def getDutyCycle(self):
		return self.currentDuty


	# Returns the pin name, duty cycle, frequency, and polarity of the attached pin
	def getPinStatus(self):
		return (self.pin, self.currentDuty, self.frequency, self.polarity)


	# Returns the list of allowed pin
	def getAllowedPins():
		return Servo.ALLOWED_PINS


	# Returns the current usage information for the allowed pins. (Tells which pins are currently in use8juuuuuuuuuuuuuuuuu)
	def getPinUsage():
		return Servo.PINS_IN_USE