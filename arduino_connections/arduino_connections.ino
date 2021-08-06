#include <Servo.h>
Servo myservo; 
char myByteArray;
int i;
void setup() {
  myservo.attach(3);
  Serial.begin(9600);
  myservo.write(60);
}

void loop()
{    

    while(Serial.available())
    {
      myByteArray = Serial.read();
      if(myByteArray=='1')
      {
        for(i=59; i!=20; i--)
        {
        myservo.write(i);
        delay(50);
        } 
      }
      if(myByteArray=='2')
      {
        myservo.write(60);
      }
      if(myByteArray=='0')
      {
        for(i=61; i!=100; i++)
        {
        myservo.write(i);
        delay(50);
        }
      }
      delay(1000);
    }
}
