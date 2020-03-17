/* get accelerate data of H3LIS331DL
 * Auth : lawliet(lawliet.zou@gmail.com)
 * version : 0.1
 */

#include <H3LIS331DL.h>
#include <H3LIS331DL.h>
#include <Wire.h>
#include <Wire.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN   7
#define CSN_PIN 8

//please get these value by running H3LIS331DL_AdjVal Sketch.
#define VAL_X_AXIS  203
#define VAL_Y_AXIS  165
#define VAL_Z_AXIS  371

#define VAL_X1_AXIS  203
#define VAL_Y1_AXIS  165
#define VAL_Z1_AXIS  371

const byte thisSlaveAddress[5] = {'R','x','A','A','A'};

H3LIS331DL h3lis;
//H3LIS331DL h3lis;
RF24 radio(CE_PIN, CSN_PIN);
const int num=3;
 int array[num];
 int array1[num];



void setup(){
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(thisSlaveAddress);
  radio.setPALevel(RF24_PA_MAX);
  radio.setDataRate(RF24_250KBPS);   
  h3lis.init();
  h3lis.importPara(VAL_X_AXIS,VAL_Y_AXIS,VAL_Z_AXIS);
  h3lis.importPara(VAL_X1_AXIS,VAL_Y1_AXIS,VAL_Z1_AXIS); 
 // pinMode(A0,INPUT);
  radio.stopListening(); 
}

void loop(){
  
  int16_t x,y,z,x1,y1,z1;
 // x=analogRead(A0);
  h3lis.readXYZ(&x,&y,&z);
  h3lis.readXYZ(&x1,&y1,&z1);
  Serial.print("x, y, z = ");
  Serial.print(x);
  Serial.print("\t");
  Serial.print(y);
  Serial.print("\t");
  Serial.println(z);
  delay(1000);
  Serial.print("x1, y1, z1 = ");
  Serial.print(x1);
  Serial.print("\t");
  Serial.print(y1);
  Serial.print("\t");
  Serial.println(z1);
  delay(1000);

  //double xyz[3];
  array[0]=x;
  array[1]=y;
  array[2]=z;

  array1[0]=x1;
  array1[1]=y1;
  array1[2]=z1;

  
  radio.write(&array,sizeof(array));
  delay(1000);
  radio.write(&array1,sizeof(array1));
  delay(1000);
  /*h3lis.getAcceleration(xyz);
  Serial.print("accelerate of x, y, z = ");
  Serial.print(xyz[0]);
  Serial.print("g");
  Serial.print("\t");
  Serial.print(xyz[1]);
  Serial.print("g");
  Serial.print("\t");
  Serial.print(xyz[2]);
  Serial.println("g");  
 
  delay(3000);*/
}
