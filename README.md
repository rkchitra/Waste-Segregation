# Waste-Segregation  
This is an embedded system project that aims to segregate any given waste material as biodegradable or non-biodegradable, using a web application. The web application has 2 primary functionalities: **(i) Capture Image (ii) Upload Image**   

### Capture Image  
The user can place a waste material on the platform, capture its image through the webcam and get the prediction. Upon prediction, the platform will rotate such that the waste material will get dumped in the appropriate bin. The waste material is placed on the platform, which is rotated using a motor. The motor is in turn connected to the arduino board which receives instructions from the laptop/computer. The arduino board is connected to the laptop/system through an Arduino USB cable and is connected to the motor through jumper cables. 

### Upload Image   
The user can browse the device for pictures and on uploading the picuture, get the prediction accordingly. 

### Miscellaneous  
There are 2 static pages namely About Us and Model Info. The About Us page talks about our motivation and inspiration for this project and the current method being employed to segregate waste. The Model Info talks about the model we've used and sheds some light on the dataset.  

## Requirements:   
• Arduino IDE  
• Installation of _**fastai, flask,jsonify,base64,numpy, cv2**_      
• Installation of the following modules: _**pathlib,glob2,sklearn,pandas,numpy,zipfile,shutil,re,seaborn**_ (to train the model)    
• Connection of Arduino board and laptop using Arduino USB cable  
• Connection of Arduino board and motor using jumper cables  
• Attach motor to platform in a way that is suitable for rotation  

## Running the Project:   
• Check arudino connections using Arduino IDE to check which port it has been connected to and modify accordingly if required in the arduino_connections.ino file, which can be found in the arduino_connections folder  
• Go to the project folder in command prompt and go to the folder named webcam  
• In command prompt, run the following command (without double quotes): _"python main.py"_  
• Open a web browser and go to http://localhost:5000 to view and run the project  
