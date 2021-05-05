from flask import Flask , request , render_template, redirect , url_for, session,flash
import jsonify 
import base64
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('signup-2.html')
@app.route('/handleimage',methods =['POST'])
def handleimage():
    if request.method == 'POST':
        print(request.form['userID'])
        print(type(request.form['file']))
        print("here")
        with open('sample.png', 'wb') as f:
            f.write(base64.decodebytes(request.form['file'].split(',')[1].encode()))
        return "Image url recieved , check console, also file wwwritten in PC hopefully"
    return "Get not allowed"
if __name__ == "__main__":
    app.run(debug=True)