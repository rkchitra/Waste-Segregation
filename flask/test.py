from flask import Flask,render_template,request,json
import numpy as np
import cv2
import re
import base64

import io

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('webcam.html')

@app.route('/disp_pic',methods = ['GET','POST'])
def disp_pic():
	if request.method == 'POST' :
		data = request.data
		#encoded_data = data.split(',')[1]
		#nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
		#img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
		#cv2.imshow(img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
	else:
		return 'success'

if __name__ == '__main__':
   app.run(debug = True)