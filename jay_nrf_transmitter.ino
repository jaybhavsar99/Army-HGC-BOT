#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#define CE_PIN  7
#define CSN_PIN 8
#include <H3LIS331DL.h>
#include <MPU6050_tockn.h>
#include <Wire.h>

//please get these value by running H3LIS331DL_AdjVal Sketch.
#define VAL_X_AXIS  66
#define VAL_Y_AXIS  9
#define VAL_Z_AXIS  72
#define Anglex
#define Angley
#define Anglez 


MPU6050 mpu6050(Wire);
H3LIS331DL h3lis;



const byte slaveAddress[5] = {'R','x','A','A','A'};
RF24 radio(CE_PIN, CSN_PIN);
int jam[6];








void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(slaveAddress);
  radio.setPALevel(RF24_PA_MAX);
 // radio.setDataRate(RF24_250KBPS);   
    radio.stopListening(); 
     h3lis.init();
  h3lis.importPara(VAL_X_AXIS,VAL_Y_AXIS,VAL_Z_AXIS);
    Wire.begin();
  mpu6050.begin();
  //mpu6050.calcGyroOffsets(true);
}


 
void loop() {
  // put your main code here, to run repeatedly:
  int16_t x,y,z;
  mpu6050.update();
  h3lis.readXYZ(&x,&y,&z);
  Serial.print("x, y, z = ");
  Serial.print(x);
  Serial.print("\t");
  Serial.print(y);
//  Serial.print("\t");
//  Serial.println(z);
  Serial.print("\tangleX : ");
  Serial.println(mpu6050.getAngleX());
  Serial.print("\tangleY : ");
  Serial.println(mpu6050.getAngleY());
//  Serial.print("\tangleZ : ");
//  Serial.println(mpu6050.getAngleZ());
    jam[0]= mpu6050.getAngleX();
    jam[1]= mpu6050.getAngleY();
    jam[2]= mpu6050.getAngleZ();
    jam[3]= x ;
    jam[4]= y ;
    jam[5]= z ;
  //radio.write(&nam,sizeof(nam));
  radio.write(&jam,sizeof(jam));
//  delay(3000);
  
}
