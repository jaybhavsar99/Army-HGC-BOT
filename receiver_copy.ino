# include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#define CE_PIN  7
#define CSN_PIN 8
#include <H3LIS331DL.h>
#include <MPU6050_tockn.h>
#include <Wire.h>
#include <Servo.h>
const byte slaveAddress[5] = {'R','x','A','A','A'};
RF24 radio(CE_PIN, CSN_PIN);
//int nam[3];
int jam[6];
int x=0;
int y =0;
int z =0;
int a =0;
int b =0;
int c =0;

void forward1(){
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
  
}
void backward1(){
  digitalWrite(3,HIGH);
  digitalWrite(2,LOW);
  
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
}

void right(){
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
}
void left(){
  digitalWrite(2,LOW);
  digitalWrite(3,HIGH);
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
}

void stop1(){
  digitalWrite(2,LOW);
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  
}

String final;

void setup() {
  // put your setup code here, to run once:
  pinMode(2,OUTPUT);
pinMode(3,OUTPUT);
pinMode(4,OUTPUT);
pinMode(5,OUTPUT);
  // put your setup code here, to run once:
    Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0,slaveAddress);
  radio.setPALevel(RF24_PA_MAX);
 // radio.setDataRate(RF24_250KBPS);   
    radio.startListening();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(radio.available())
  { 
    //radio.read(&nam,sizeof(nam));
     radio.read(&jam,sizeof(jam));
    a=jam[0]; 
    b=jam[1] ;
    c=jam[2];
    x=jam[3];
    y=jam[4] ;
    z=jam[5] ;
    
  String final ="";
  final += a;
  final +=":";
  final +=b;
  final += ":";
  final += c;
  final +=":";

  final += x;
  final +=":";
  final += y;
  final +=":";
  final += z;

  Serial.println(final);
  if(b>45){
      forward1();
      
      Serial.print("moving forward");
      delay(300);
  }
  else if(b<-45){
    backward1();
    
    Serial.print("moving backward");
    delay(300);
  }
  if(a>45){
    right();
    Serial.print("moving right");
    delay(300);
  }
  else if(a<-45){
    left();
    Serial.print("moving left");
    delay(300);
  }
  if(-45<a<45 && -45<b<45){
    stop1();
   // delay(30);
  }
  }
}
