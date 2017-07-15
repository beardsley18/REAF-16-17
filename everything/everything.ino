//EDITED: 5/22
//Arduino doesn’t like the * symbol so changed it to a 0 instead.
//torpedo and marble states were changed to volatile 


/*THIS IS THE SKELETON FOR THE FINAL CODE INCLUDING 8 THRUSTERS AND 6 SERVOS 
 Feel free to correct spelling errors, I'm an engineer not an english major */

//Include the arduino servo library with all of the servo commands 
#include <Servo.h>

//Thrusters
Servo sda;
Servo sdf;
Servo sv0;
Servo sm0;
Servo pdf;
Servo pda;
Servo pm0;
Servo pv0;

//Servos
/*Servo cf;
Servo cw;
Servo m1;
Servo m2;
Servo t1;
Servo t2;*/

//set boolean for if executed
/*volatile bool torpedoa = false;
volatile bool torpedob = false;
volatile bool marblea = false;
volatile bool marbleb= false;*/

/*Thruster speed values (edit once tested with sub)
1100 is max reverse value, 1500 is stop, 1900 is max forward*/
int reverse_fast = 1200;
int reverse_slow = 1400;
int stop_moving = 1500;
int forward_slow = 1600;
int forward_fast = 1800;

int sda_speed = stop_moving;
int sdf_speed = stop_moving;
int sv0_speed = stop_moving;
int sm0_speed = stop_moving;
int pdf_speed = stop_moving;
int pda_speed = stop_moving;
int pm0_speed = stop_moving;
int pv0_speed = stop_moving;

int switchPin = 24;
int switchState = 0; // whether the switch is on or off
  
//Setup, only runs at beginning and does not run again
void setup() {
  //Serial monitor setup
  Serial.begin(9600);
  //while(!Serial);
  //Serial.println("Ready for commands.");

  /*Thuster set up
  Connect thrusters to pins, can be changed when needed
  PWM on mega is pins 2-13 */
  sda.attach(2);
  sdf.attach(4);
  sv0.attach(6);
  sm0.attach(8);
  pdf.attach(10);
  pda.attach(12);
  pm0.attach(3);
  pv0.attach(5);

  /*Servo set up
  Connect servos to pins, can also be changed when needed */
  /*cf.attach(10);
  cw.attach(11);
  m1.attach(12);
  m2.attach(13);
  //PWM is also pins 44 - 46
  t1.attach(44);
  t2.attach(45);*/

  //set switch pin as input
  pinMode(switchPin, INPUT);
  
  //Thrusters have to initialized with 1500 microseconds and must include delay of 1000 ms for the ESC to recognize it
  sda.writeMicroseconds(sda_speed);
  sdf.writeMicroseconds(sdf_speed);
  sv0.writeMicroseconds(sv0_speed);
  sm0.writeMicroseconds(sm0_speed);
  pdf.writeMicroseconds(pdf_speed);
  pda.writeMicroseconds(pda_speed);
  //pm0.writeMicroseconds(pm0_speed);
  //pv0.writeMicroseconds(pv0_speed);
  delay(1000);
}

void loop() {
  switchState = digitalRead(switchPin);
  /*ACTUAL MOVEMENT AND MECHANISMS, EDIT AS NEEDED
  all functions must be inside loop for serial commands */
  if (Serial.available() > 0) {
    //assign what is in serial monitor as command
    char inputBuffer[3];
    int b = Serial.readBytes(inputBuffer, 3);
    //break down command into 4 parts, char 1, char 2, char 3, and speed 
    //currently not reading speed
    /*test NUC communication
    if (strcmp(inputBuffer, "FOR") == 1) {
      Serial.write(inputBuffer, 3);
    }
    else {
      Serial.write("NOP");
    }*/
    if (switchState == LOW) {
      sda_speed = stop_moving;
      sdf_speed = stop_moving;
      sv0_speed = stop_moving;
      sm0_speed = stop_moving;
      pdf_speed = stop_moving;
      pda_speed = stop_moving;
      pm0_speed = stop_moving;
      pv0_speed = stop_moving;
      Serial.write("NON", 3);
    }
    else {
      //cases for thrusters *NEEDS EDITING
      //general commands                                                                                                                                                                                                  c
      if (strcmp(inputBuffer, "FOR") == 1) {
        /*pm0.writeMicroseconds(forward_slow);
        delay(1000);
        pv0.writeMicroseconds(forward_slow);
        delay(1000);
        sm0.writeMicroseconds(forward_slow);
        delay(1000);
        sv0.writeMicroseconds(forward_slow);
        delay(1000);
        */
        sda_speed = stop_moving;
        sdf_speed = stop_moving;
        sv0_speed = forward_slow;
        sm0_speed = forward_slow;
        pdf_speed = stop_moving;
        pda_speed = stop_moving;
        pm0_speed = forward_slow;
        pv0_speed = forward_slow;
        Serial.write("FOR", 3);
        //Serial.write("Sub moving forward"); //edit for specific command, add LED command
      }
      else if (strcmp(inputBuffer, "BAC") == 1) {
        /*pm0.writeMicroseconds(reverse_slow);
        delay(1000);
        pv0.writeMicroseconds(reverse_slow);
        delay(1000);
        sm0.writeMicroseconds(reverse_slow);
        delay(1000);
        sv0.writeMicroseconds(reverse_slow);
        delay(1000);*/
        sda_speed = stop_moving;
        sdf_speed = stop_moving;
        sv0_speed = reverse_slow;
        sm0_speed = reverse_slow;
        pdf_speed = stop_moving;
        pda_speed = stop_moving;
        pm0_speed = reverse_slow;
        pv0_speed = reverse_slow;
        Serial.write("BAC");
        //Serial.println("Sub moving backward"); //edit for specific command, add LED command
      }
      else if (strcmp(inputBuffer, "UP*") == 1) {
        /*sdf.writeMicroseconds(forward_slow);
        delay(1000);
        sda.writeMicroseconds(forward_slow);
        delay(1000);
        pda.writeMicroseconds(forward_slow);
        delay(1000);
        pdf.writeMicroseconds(forward_slow);
        delay(1000);
        */
        sda_speed = forward_slow;
        sdf_speed = forward_slow;
        sv0_speed = stop_moving;
        sm0_speed = stop_moving;
        pdf_speed = forward_slow;
        pda_speed = forward_slow;
        pm0_speed = stop_moving;
        pv0_speed = stop_moving;
        Serial.write("UP*");
        //Serial.println("Sub moving up"); //edit for specific command, add LED command
      }
      else if (strcmp(inputBuffer, "DOW") == 1) {
        /*sdf.writeMicroseconds(reverse_slow);
        delay(1000);
        sda.writeMicroseconds(reverse_slow);
        delay(1000);
        pda.writeMicroseconds(reverse_slow);
        delay(1000);
        pdf.writeMicroseconds(reverse_slow);
        delay(1000);*/
        sda_speed = reverse_slow;
        sdf_speed = reverse_slow;
        sv0_speed = stop_moving;
        sm0_speed = stop_moving;
        pdf_speed = reverse_slow;
        pda_speed = reverse_slow;
        pm0_speed = stop_moving;
        pv0_speed = stop_moving;
        Serial.write("DOW");
        //Serial.println("Sub moving down"); //edit for specific command, add LED command
      }
      else if (strcmp(inputBuffer, "RIG") == 1) {
        /*pm0.writeMicroseconds(forward_slow);
        delay(1000);
        pv0.writeMicroseconds(forward_slow);
        delay(1000);*/
        sda_speed = stop_moving;
        sdf_speed = stop_moving;
        sv0_speed = stop_moving;
        sm0_speed = stop_moving;
        pdf_speed = stop_moving;
        pda_speed = stop_moving;
        pm0_speed = forward_slow;
        pv0_speed = forward_slow;
        Serial.write("RIG");
        //Serial.println("Sub moving right"); //edit for specific command, add LED command
      } 
      else if (strcmp(inputBuffer, "LEF") == 1) {
        /*sm0.writeMicroseconds(forward_slow);
        delay(1000);
        sv0.writeMicroseconds(forward_slow);
        delay(1000);*/
        sda_speed = stop_moving;
        sdf_speed = stop_moving;
        sv0_speed = forward_slow;
        sm0_speed = forward_slow;
        pdf_speed = stop_moving;
        pda_speed = stop_moving;
        pm0_speed = stop_moving;
        pv0_speed = stop_moving;
        Serial.write("LEF");
        //Serial.println("Sub moving left"); //edit for specific command, add LED command
      }
      else if (strcmp(inputBuffer, "HOV") == 1) {
        /*sda.writeMicroseconds(forward_slow);
        delay(1000);
        sdf.writeMicroseconds(forward_slow);
        delay(1000);
        pda.writeMicroseconds(forward_slow);
        delay(1000);
        pdf.writeMicroseconds(forward_slow);
        delay(1000);*/
        sda_speed = forward_slow;
        sdf_speed = forward_slow;
        sv0_speed = stop_moving;
        sm0_speed = stop_moving;
        pdf_speed = forward_slow;
        pda_speed = forward_slow;
        pm0_speed = stop_moving;
        pv0_speed = stop_moving;
        Serial.write("HOV");
        //Serial.println("Sub hovering"); //edit for specific command, add LED command
      }
      else {
        Serial.write("NON");
      }
       
      //indivudal commands 
      //switch case for mechanisms
      /*switch (command) { 
        case t1: 
          if (torpedoa == false) {
            //launch torpedo
            torpedoa = true;
            Serial.println("First torpedo launched"); 
          }
          else {
            Serial.println("Torpedo A already launched"); //edit for specific command, add LED command
          break;
          } 
        case t2: 
          if (torpedob == false) {
            //launch torpedo
            torpedob = true;
            Serial.println("Second torpedo launched"); 
          }
          else {
            Serial.println("Torpedo B already launched"); //edit for specific command, add LED command
          break;
          }
        case cf: 
          cf.write(100); //open
          delay(1000); //wait
          cf.write(450); //close
          Serial.println("Claw grabbed"); 
          break;
       case cw: 
          //move wrist
          Serial.println("Claw angle changed"); 
          break;
       case m1: 
          if (marblea == false) {
            //drop marble
            marblea = true;
            Serial.println("First marble droppped"); 
          }
          else {
            Serial.println("Marble A already dropped"); //edit for specific command, add LED command
          break;
          }
        case m2: 
          if (marbleb == false) {
            //drop marble
            marbleb = true;
            Serial.println("Second marble dropped"); 
          }
          else {
            Serial.println("Marble B already dropped"); //edit for specific command, add LED command
          break;
          }
    }*/
    } // end if (switchState == HIGH)
  } //end if (Serial.available() > 0)

  sda.writeMicroseconds(sda_speed);
  sdf.writeMicroseconds(sdf_speed);
  sv0.writeMicroseconds(sv0_speed);
  sm0.writeMicroseconds(sm0_speed);
  pdf.writeMicroseconds(pdf_speed);
  pda.writeMicroseconds(pda_speed);
  //pm0.writeMicroseconds(pm0_speed);
  //pv0.writeMicroseconds(pv0_speed);
  delay(1000);

  /*COMMANDS
    Thrusters
      NAME.writeMircroseconds(speed);
      delay(1000); **for ESC recognition
    Servos
      Claw
        Claw_finger.write(100); ** open
        Claw_finger.write(450); ** close
  */
} //end loop
