#include <Servo.h>

byte servoPin = 9;
Servo servo;


void setup() {
  servo.attach(servoPin);

  servo.writeMicroseconds(1500); // send "stop" signal to ESC.
  delay(1000); // delay to allow the ESC to recognize the stopped signal
  Serial.begin(9600);
  while(!Serial); //make sure serial interface is done initializing - may not be necessary
  pinMode(LED_BUILTIN, OUTPUT);
}
//int incomingByte = 0;



void loop() {
  /*if(incomingByte == 0){
    Serial.println("something");
    incomingByte = 1;
  }*/
  //if (Serial.available() >= 2) {
  if (Serial.available() > 0) {
                // read the incoming byte:
//                while (Serial.available() > 0) {
//                incomingByte = Serial.read();
//                Serial.write(incomingByte);
//                }
                //int b = Serial.read();
                char inputBuffer[3];
                int b = Serial.readBytes(inputBuffer, 3);
                char confirm = 'y';
                /*if(inputBuffer == "111"){
                  confirm = '1';
                }
                if(inputBuffer == "222"){
                  confirm = '2';
                }
                if(inputBuffer == "333"){
                  confirm = '3';
                }
                if(inputBuffer == "000"){
                  confirm = '0';
                }*/
                //Serial.println("r");
                //Serial.write("r");
                //int c = Serial.read();
                //Serial.write(3);
                Serial.write(inputBuffer);
                //Serial.write(c);
                // say what you got:
//                int a = Serial.available();
//                Serial.print(a);
//                Serial.print("I received: ");
//                Serial.println(incomingByte, DEC); //returns a string of the ASCII value of the last character in the string
        }
//        else
//            Serial.println("Not received");
            
  int signal = 1700; // Set signal value, which should be between 1100 and 1900
  
  delay(250); //Controls output speed

  servo.writeMicroseconds(signal); // Send signal to ESC.
}



