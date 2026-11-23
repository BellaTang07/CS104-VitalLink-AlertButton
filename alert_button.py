import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Alert button monitoring systen is now active. Press Ctrl+c to stop.")

button_pressed = True
try:
	while True:
		if GPIO.input(7) == GPIO.HIGH:
			print("Someone pressed the alert button!")
		elif GPIO.input(7) == GPIO.LOW:
			button_pressed = False
		time.sleep(0.1)
except KeyboardInerrupt:
		print("\nMonitoring stoppped.")
		GPIO.cleanup()
