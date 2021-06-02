from flask import Flask , request , render_template, redirect , url_for, session,flash
import jsonify 
import base64
import serial
import time
def setuparduino():
	arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1) 
	print("Setting up arduino....")
	time.sleep(4)
	print("Arduino connected")
	return arduino
def left(arduino):
	arduino.write(b'1')
def start(arduino):
	arduino.write(b'2')
def right(arduino):
	arduino.write(b'0')
def movebiodegradabe():
	ard = setuparduino()
	right(ard)
	time.sleep(5)
	start(ard)
	ard.close()
def movenonbiodegradabe():
	ard = setuparduino()
	left(ard)
	time.sleep(5)
	start(ard)
	ard.close()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	movenonbiodegradabe()
	return render_template('signup-2.html')
@app.route('/handleimage',methods =['POST'])
def handleimage():
    if request.method == 'POST':
        print(type(request.form['file']))
        print("here")
        movebiodegradabe()
        with open('sample.png', 'wb') as f:
            f.write(base64.decodebytes(request.form['file'].split(',')[1].encode()))
        return "Image url recieved , check console"
    return "Get not allowed"
if __name__ == "__main__":
    app.run(debug=True)