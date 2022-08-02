
//https://console.firebase.google.com/u/0/project/led-blink-wifi/database/led-blink-wifi-default-rtdb/data
//https://page-view-7a557-default-rtdb.asia-southeast1.firebasedatabase.app/

#include <ESP8266WiFi.h>
#include "FirebaseESP8266.h"

int servoPin = 2;

#define WIFI_SSID "OPPO A31"
#define WIFI_PASSWORD "12345678"

#define FIREBASE_HOST "page-view-7a557-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "bPEoRnnXW1ssubiKTbQG0TupJ9IO7AYGtw3QWFXO"

FirebaseData firebaseData;

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");

  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }

  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);

  //Set database read timeout to 1 minute (max 15 minutes)
  Firebase.setReadTimeout(firebaseData, 1000 * 60);

  pinMode(servoPin, OUTPUT);
}

void loop() {

    if (Firebase.getInt(firebaseData,"/iot/tubelight")) {
      int val2 = (firebaseData.intData());
      if(val2==1){
        digitalWrite(servoPin, LOW);
        Serial.println("HIGH");
      }else{
        digitalWrite(servoPin, HIGH);
        Serial.println("LOW");
      }
    }

    delay(200);
}
