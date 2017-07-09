#include <Servo.h>

Servo servo;

void setup() {
  Serial.begin(9600);
  //while(!Serial);
  servo.attach(6);

  //servo.writeMicroseconds(1500);
  //delay(1000);
}

void loop() {
  if (Serial.available() > 0) {
      char inputBuffer[3];
      int b = Serial.readBytes(inputBuffer, 3);
      if (strcmp(inputBuffer, "FOR") == 0) {
        Serial.write(inputBuffer, 3);
      }
      else {
        Serial.write("NOP");
      }
  }
  //servo.writeMicroseconds(1700);
}
