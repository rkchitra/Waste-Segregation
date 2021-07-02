#include <Servo.h>
Servo myservo; 
char myByteArray;  
int i;
void setup() {
  myservo.attach(3);    #attaching server motor to pin 3 of arduino
    
  Serial.begin(9600);   #opening a connection at the port 9600 so that python code can communicate with Arduino
  myservo.write(60);    # setting up the arduino starting at the middle position
}

void loop()
{    

    while(Serial.available())
    {
      myByteArray = Serial.read(); #reading what python script wrote in the communicating serial connection
      if(myByteArray=='1')
      {
        for(i=59; i!=20; i--)   #tilting the platform left
        {
        myservo.write(i);
        delay(50);
        } 
      }
      if(myByteArray=='2')  # bringing arduino to initial position
      {
        myservo.write(60);
      }
      if(myByteArray=='0')
      {
        for(i=61; i!=100; i++) #tilting right
        {
        myservo.write(i);
        delay(50);
        }
      }
      delay(1000);
    }
}
