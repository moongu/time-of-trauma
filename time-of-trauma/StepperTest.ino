#include <Wire.h>
#include <Adafruit_MotorShield.h>

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield();

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(513, 2);


void setup() {
  Serial.begin(9600);
  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
  myMotor->setSpeed(1);
}

void loop() {
  Serial.println("Single coil steps");
  myMotor->step(200, FORWARD, SINGLE);

  //Serial.println("Double coil steps");
  //myMotor->step(600, FORWARD, DOUBLE);
  
  //Serial.println("Interleave coil steps");
  //myMotor->step(600, FORWARD, INTERLEAVE);
  
  //Serial.println("Microstep steps");
  //myMotor->step(600, FORWARD, MICROSTEP);
}
