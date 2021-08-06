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
from transform_image import transform,transform2
def setuparduino():
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) 
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
app = Flask(__name__,static_url_path='/static')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route('/handleimage',methods =['POST'])
def handleimage():
    if request.method == 'POST': 
        ran = generate_filename() 
        with open("static/pics_for_prediction/"+ran, 'wb') as f:
            f.write(base64.decodebytes(request.form['file'].split(',')[1].encode()))
            #print("Image name: ",ran)
        print("Image name:")
        trans_ran = transform(ran)
        print("Transformation Complete")
        pred = predict_waste(trans_ran)
        #if pred=='nonbiodegradable':
        #    movenonbiodegradabe()
        #elif pred == 'biodegradable' :
        #    movebiodegradabe()
        pred = pred[0]
        pred = pred + ran
        return pred
@app.route('/upload',methods = ['GET','POST'])
def upload() :
    return render_template('upload.html')
@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      fname = generate_filename()
      f.save("static/pics_for_prediction/"+fname)
      print("Saved file")
      trans_ran = transform2(fname)
      print("Ran transform function")
      pred = predict_waste(trans_ran)[0]
      #if pred == 'n' :
      #  movenonbiodegradabe()
      #else :
      #  movebiodegradabe()
      pred = pred + fname
      return pred


@app.route('/nonbio')
def nbio() :
    movenonbiodegradabe()
    return "hello"

@app.route('/bio')
def bio() :
    movebiodegradabe()
    return "bye"

@app.route('/aboutus')
def about() :
    return render_template('about_us.html')
@app.route('/model_info')
def minfo() :
    return render_template('model_info.html')

def generate_filename() :
    S = 10
    # call random.choices() string module to find the string in lowercase + numeric data. 
    ran = ''.join(random.choices(string.ascii_lowercase+ string.digits, k = S))+'.png'
    while path.exists(ran) :
            ran = ''.join(random.choices(string.ascii_lowercase+ string.digits, k = S))+'.png'
    return ran


if __name__ == "__main__":
    app.run(debug=True)