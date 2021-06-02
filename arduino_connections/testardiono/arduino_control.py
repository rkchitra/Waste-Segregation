import serial
import time
arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1) 
print("Setting up arduino....")
time.sleep(4)
print("Arduino connected")
def left():
	arduino.write(b'1')
def start():
	arduino.write(b'2')
def right():
	arduino.write(b'0')
start()
def movebiodegradabe():
	right()
	time.sleep(5)
	start()
def movenonbiodegradabe():
	left()
	time.sleep(5)
	start()
movenonbiodegradabe()
movebiodegradabe()