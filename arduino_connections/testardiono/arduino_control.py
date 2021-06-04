import serial
import time
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) 
print("Setting up arduino....")
time.sleep(4)
print(arduino)
print("Arduino connected")
def left():
	arduino.write(b'1')
	time.sleep(5)
	start()
def start():
	arduino.write(b'2')
def right():
	arduino.write(b'0')
	time.sleep(5)
	start()
start()
def movebiodegradabe():
	right()
def movenonbiodegradabe():
	left()
#movenonbiodegradabe()
#movebiodegradabe()
left()
right()
right()
left()