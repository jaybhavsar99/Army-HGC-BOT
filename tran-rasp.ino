#include "RF24.h"
#include "nRF24L01.h"
#include "RF24.h"

RF24 radio(9, 10);
const uint64_t data_pipe[1] = {0xF0F0F0F0E1};

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.setRetries(15, 15);
  radio.setPayloadSize(32);
  radio.setChannel(0x76);
  radio.setPALevel(RF24_PA_MIN);
  radio.openWritingPipe(data_pipe);
  radio.enableDynamicPayloads();

}

void loop() {
  radio.stopListening();
  char data[] = "1234567890";
  Serial.println("");
  Serial.print("Data: ");
  Serial.println(data);
  Serial.print("sizeof(data): ");
  Serial.println(sizeof(data));
  radio.write(&data, sizeof(data));
  Serial.println("Data send");
  delay(1000);
}
