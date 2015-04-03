#include <SoftwareSerial.h>
#include <Servo.h> 
SoftwareSerial Genotronex(0, 1); // RX, TX
int BluetoothData; // the data given from Computer
Servo myservo;
Servo myservo1;

 void motor() {
 
  myservo.write(0);
  delay(1500);
  myservo.write(360);
  delay(1500);
  myservo.write(90);
  
}

 void motor1() {
 
  myservo1.write(0);
  delay(1000);
  myservo1.write(120);
  delay(2000);
  myservo1.write(90);
  
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myservo.attach(5); 
  myservo1.attach(6); 
  Genotronex.begin(9600);
  pinMode(7, OUTPUT);
}

void loop() {
  
   if (Genotronex.available()){
    BluetoothData=Genotronex.read();
    
     if(BluetoothData=='0'){ 
   Serial.println("0");  // if number 1 pressed ....
   motor1();
   
   }
    
   if(BluetoothData=='1'){ 
   Serial.println("1");  // if number 1 pressed ....
   motor1();
   }
  
  if (BluetoothData=='2'){
    Serial.println("2");// if number 0 pressed ....
  }
  
  if (BluetoothData=='3'){
    Serial.println("3");// if number 0 pressed ....
  }
  
   if (BluetoothData=='4'){
    Serial.println("4");// if number 0 pressed ....
  }
  
  if (BluetoothData=='5'){
    Serial.println("5");// if number 0 pressed ....
    motor();
  }
  
  if (BluetoothData=='6'){
    Serial.println("6");// if number 0 pressed ....
    motor1();
    motor();
  }
  
  if (BluetoothData=='7'){
    Serial.println("7");// if number 0 pressed ....
    motor1();
    motor();
  }
  
  if (BluetoothData=='8'){
    Serial.println("8");// if number 0 pressed ....
    motor();
  }
  
  if (BluetoothData=='9'){
    Serial.println("music1");// if number 0 pressed ....
    motor();
  }
  
  if (BluetoothData=='d'){
    Serial.println("music2");// if number 0 pressed ....
  }
  
   if (BluetoothData=='m'){
    Serial.println("music3");// if number 0 pressed ....
    motor();
    motor();
    motor();
  }
  
   if (BluetoothData=='s'){
     
    Serial.println("stop");// if number 0 pressed ....
    motor();
    
  }
  
   if (BluetoothData=='v'){
    // if number 0 pressed ....
   
    digitalWrite(7, HIGH);
    Serial.println("vvv");   // turn the LED on (HIGH is the voltage level)
    delay(3000);
    digitalWrite(7, LOW);   // 
  }
}
delay(100);// prepare for next data ...
}

