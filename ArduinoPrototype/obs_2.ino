#include<Servo.h>

int sev = 7; 
int trig = 11;
int echo =10;
int IR =8;

Servo servo;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(8,INPUT);
servo.attach(7);

pinMode(trig, OUTPUT);
pinMode(echo, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

 servo.write(90);
 long duration, distance;
 digitalWrite(trig, HIGH);
 delayMicroseconds(700);
 digitalWrite(trig, LOW);
 duration=pulseIn(echo,HIGH);
 distance =(duration/2)/29.1;
 Serial.print(distance);
 Serial.println("CM");
 delay(1000);
 
int detect = digitalRead(8);

if (detect == LOW){
  Serial.println("Obstacle on way");
  servo.write(30);
  delay(1000);
  
  servo.write(90);
  
}
if( distance >95){
  servo.write(30);
  delay(1000);

  servo.write(90);
}
}
