#include <Servo.h>

byte servoPin1 = 2;
Servo servo1;
byte servoPin2 = 4;
Servo servo2;
byte servoPin3 = 6;
Servo servo3;
byte servoPin4 = 8;
Servo servo4;
byte servoPin5 = 10;
Servo servo5;
byte servoPin6 = 12;
Servo servo6;
/*byte servoPin7 = 9;
Servo servo7;
byte servoPin8 = 9;
Servo servo8;*/

void setup() {
  servo1.attach(servoPin1);
  servo2.attach(servoPin2);
  servo3.attach(servoPin3);
  servo4.attach(servoPin4);
  servo5.attach(servoPin5);
  servo6.attach(servoPin6);
  /*servo7.attach(servoPin7);
  servo8.attach(servoPin8);*/

  servo1.writeMicroseconds(1500); // send "stop" signal to ESC.
  //delay(1000); // delay to allow the ESC to recognize the stopped signal
  servo2.writeMicroseconds(1500); // send "stop" signal to ESC.
  //delay(1000); // delay to allow the ESC to recognize the stopped signal
  servo3.writeMicroseconds(1500); // send "stop" signal to ESC.
  //delay(1000); // delay to allow the ESC to recognize the stopped signal
  servo4.writeMicroseconds(1500); // send "stop" signal to ESC.
  //delay(1000); // delay to allow the ESC to recognize the stopped signal
  servo5.writeMicroseconds(1500); // send "stop" signal to ESC.
  //delay(1000); // delay to allow the ESC to recognize the stopped signal
  servo6.writeMicroseconds(1500); // send "stop" signal to ESC.
  delay(1000); // delay to allow the ESC to recognize the stopped signal
  /*servo7.writeMicroseconds(1500); // send "stop" signal to ESC.
  delay(1000); // delay to allow the ESC to recognize the stopped signal
  servo8.writeMicroseconds(1500); // send "stop" signal to ESC.
  delay(1000); // delay to allow the ESC to recognize the stopped signal
  */
}

void loop() {
  int signal = 1600; // Set signal value, which should be between 1100 and 1900

  servo1.writeMicroseconds(signal); // Send signal to ESC.
  servo2.writeMicroseconds(signal); // Send signal to ESC.
  servo3.writeMicroseconds(signal); // Send signal to ESC.
  servo4.writeMicroseconds(signal); // Send signal to ESC.
  servo5.writeMicroseconds(signal); // Send signal to ESC.
  servo6.writeMicroseconds(signal); // Send signal to ESC.
  /*servo7.writeMicroseconds(signal); // Send signal to ESC.
  servo8.writeMicroseconds(signal); // Send signal to ESC.*/
}
