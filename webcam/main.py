from flask import Flask , request , render_template, redirect , url_for, session,flash
import jsonify 
import base64
import serial
import time
import string    
import random
import os.path
from os import path
from load import predict_waste
from transform_image import transform
#def setuparduino():
#	arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) 
#	print("Setting up arduino....")
#	time.sleep(4)
#	print("Arduino connected")
#	return arduino
#def left(arduino):
#	arduino.write(b'1')
#def start(arduino):
#	arduino.write(b'2')
#def right(arduino):
#	arduino.write(b'0')
#def movebiodegradabe():
#	ard = setuparduino()
#	right(ard)
#	time.sleep(5)
#	start(ard)
#	ard.close()
#def movenonbiodegradabe():
#	ard = setuparduino()
#	left(ard)
#	time.sleep(5)
#	start(ard)
#	ard.close()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	#movenonbiodegradabe()
	return render_template('signup-2.html')
@app.route('/handleimage',methods =['POST'])
def handleimage():
    if request.method == 'POST':
        #print(type(request.form['file']))
        #movebiodegradabe()
        S = 10   
        # call random.choices() string module to find the string in lowercase + numeric data.  
        ran = ''.join(random.choices(string.ascii_lowercase+ string.digits, k = S))+'.png' 
        while path.exists(ran) :
            ran = ''.join(random.choices(string.ascii_lowercase+ string.digits, k = S))+'.png' 
        with open("pics_for_prediction/"+ran, 'wb') as f:
            f.write(base64.decodebytes(request.form['file'].split(',')[1].encode()))
            #print("Image name: ",ran)
        print("Image name:")
        trans_ran = transform(ran)
        print("Transformation Complete")
        pred = predict_waste(trans_ran)
        return pred
    return "Get not allowed"
if __name__ == "__main__":
    app.run(debug=True)