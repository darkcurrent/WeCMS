
// This code is inspired by the user victoryking. You can visit his repository with this link: https://github.com/jayraj4021/Personal-Weather-Station-14

#include <Wire.h>
#include <Adafruit_BMP085.h>
#include "ClosedCube_HDC1080.h"
#include <Adafruit_ADS1015.h>
#include <SoftwareSerial.h>

#define DEBUG 1

ClosedCube_HDC1080 hdc1080;
Adafruit_BMP085 bmp;
Adafruit_ADS1115 ads;

SoftwareSerial esp8266Module(10, 11);

String network = "--------";
String password = "--------";
#define IP "184.106.153.149"
String GET = "GET /update?api_key=----------------";

void setup()
{
  if (DEBUG) {
    Serial.begin(115200);                             // Setting hardware serial baud rate to 9600
  }
  if (!bmp.begin()) {
    if (DEBUG) {
      Serial.println("Could not find a valid BMP085 sensor, check wiring!");
    }
    while (1) {}
  }
  esp8266Module.begin(9600);
  hdc1080.begin(0x40);
  ads.begin();
  setupEsp8266();
}

void loop()
{
  //-----Measured Values-----
  float temp = hdc1080.readTemperature();
  float hum = hdc1080.readHumidity();
  float pressure = bmp.readPressure() / 100.0;
  int16_t adc0 = ads.readADC_SingleEnded(0);
  //-----Calculated Values-----
  float dewP = dewPointFast(temp, hum);
  float cloudBase = ((temp - dewP) * 400.0) * 0.3048;
  float adc0Volts = adc0 * (6.144 / 32767.0);
 /* if (DEBUG) {
    Serial.print(temp);      Serial.print(",");
    Serial.print(hum);       Serial.print(",");
    Serial.print(pressure);  Serial.print(",");
    Serial.print(adc0Volts);      Serial.print(",");
    Serial.print(dewP);      Serial.print(",");
    Serial.println(cloudBase); //Serial.print(",");
  }*/
  updateTemp(String(temp),String(hum),String(pressure),String(adc0),String(dewP),String(cloudBase),String(adc0Volts));
  delay(20000);
}

double dewPointFast(double celsius, double humidity) {
  double a = 17.271;
  double b = 237.7;
  double temp = (a * celsius) / (b + celsius) + log(humidity * 0.01);
  double Td = (b * temp) / (a - temp);
  return Td;
}

void setupEsp8266()
{
  if (DEBUG) {
    Serial.println("Reseting esp8266");
  }
  esp8266Module.flush();
  esp8266Module.println(F("AT+RST"));
  delay(7000);
  if (esp8266Module.find("OK"))
  {
    if (DEBUG) {
      Serial.println("Found OK");
      Serial.println("Changing espmode");
    }
    esp8266Module.flush();
    changingMode();
    delay(5000);
    esp8266Module.flush();
    connectToWiFi();
  }
  else
  {
    if (DEBUG) {
      Serial.println("OK not found");
    }
  }
}

//-------------------------------------------------------------------
// Following function sets esp8266 to station mode
//-------------------------------------------------------------------
bool changingMode()
{
  esp8266Module.println(F("AT+CWMODE=1"));
  if (esp8266Module.find("OK"))
  {
    if (DEBUG) {
      Serial.println("Mode changed");
    }
    return true;
  }
  else if (esp8266Module.find("NO CHANGE")) {
    if (DEBUG) {
      Serial.println("Already in mode 1");
    }
    return true;
  }
  else
  {
    if (DEBUG) {
      Serial.println("Error while changing mode");
    }
    return false;
  }
}

//-------------------------------------------------------------------
// Following function connects esp8266 to wifi access point
//-------------------------------------------------------------------
bool connectToWiFi()
{
  if (DEBUG) {
    Serial.println("inside connectToWiFi");
  }
  String cmd = F("AT+CWJAP=\"");
  cmd += network;
  cmd += F("\",\"");
  cmd += password;
  cmd += F("\"");
  esp8266Module.println(cmd);
  delay(15000);

  if (esp8266Module.find("OK"))
  {
    if (DEBUG) {
      Serial.println("Connected to Access Point");
    }
    return true;
  }
  else
  {
    if (DEBUG) {
      Serial.println("Could not connect to Access Point");
    }
    return false;
  }
}

//-------------------------------------------------------------------
// Following function sends sensor data to thingspeak.com
//-------------------------------------------------------------------
void updateTemp(String voltage1, String voltage2, String voltage3, String voltage4, String voltage5, String voltage6, String voltage7)
{
  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += IP;
  cmd += "\",80";
  esp8266Module.println(cmd);
  delay(5000);
  if (esp8266Module.find("Error")) {
    if (DEBUG) {
      Serial.println("ERROR while SENDING");
    }
    return;
  }
  cmd = GET + "&field1=" + voltage1 + "&field2=" + voltage2 + "&field3=" + voltage3 + "&field4=" + voltage4 + "&field5=" + voltage5 + "&field6=" + voltage6 + "&field7=" + voltage7 + "\r\n";
  esp8266Module.print("AT+CIPSEND=");
  esp8266Module.println(cmd.length());
  delay(15000);
  if (esp8266Module.find(">"))
  {
    esp8266Module.print(cmd);
    if (DEBUG) {
      Serial.println("Data sent");
    }
  } else
  {
    esp8266Module.println("AT+CIPCLOSE");
    if (DEBUG) {
      Serial.println("Connection closed");
    }
  }
}


