# WeCMS
WeCMS stands for Weather and Climate Monitoring Station. It is a homemade IoT weather station made using an Arduino. It has currently a temperature, a humidity and a barometric pressure sensor. I have also connected an analog ambient IR light sensor through a 16 bit DAC. For the temperature and humidity sensor I am using the __HDC1080__, for the barometric pressure sensor I am using the __BMP180__ and for the ambient IR light sensor I am using a simple __IR photodiode__. When it comes to the DAC, I am using the __ADS1115__ from Texas Instruments. Also I am using an __ESP8266__ for the wireless data transmission.
## Hardware
### What you will need
- 1x Arduino
- 1x HDC1080
- 1x BMP180
- 1x IR photodiode
- 1x ADS1115
- 1x ESP8266
### Circuit
Before you start doing anything with the software you need to make the circuit. I have not published yet the circuit but it is pretty straight forward. Both the __HDC1080__, the __BMP180__ and __ADS1115__ (the IR sensor as it is connected to the ADC) use the __I2C__ communication protocol. That means that they need only 4 wires: __VCC__,__GND__,__SDA__ and __SCL__ but the __ADS1115__ needs another connection from __ADDR__ to __GND__. Finally you need to connect the __ESP8266__ the usual way to pins 10 and 11 but I will not describe it here.
## Software
### Libraries
The code I developed uses the following 5 libraries:
```
Wire
Adafruit_BMP085
ClosedCube_HDC1080
Adafruit_ADS1015
SoftwareSerial
```
If any of these libraries is missing the code will not compile.
### Things to do before uploading the code
Before uploading the code to the Arduino you will need to change some parts of it. You need to change the dashes of the following part of code to your wifi network name and password.
```
String network = "--------";
String password = "--------";
```
You need to also change the dashes of the following part of code to your ThingSpeak API key.
```
String GET = "GET /update?api_key=----------------";
```
### Upload!
Now you are ready to upload the code to your Arduino! Enjoy your all-new personal ThingSpeak connected Arduino weather station. 

## Data Handling and Plotting

The WeCMS collects the values of the sensors and sents them to ThingSpeak. From there you can view the data as graphs but these graphs are not customizable and most importantly they demand a powerful computer. So I came up with a python program that downloads the data from ThingSpeak, re-plots them and saves them as .jpg images. These graphs are more customizable and since they are just a .jpg the do not demand a powerful computer to be viewed, but there is a catch. You can only see the new graphs from your computer. You need to host these graphs somewhere. I have chosen to do that with Dropbox. It is free and it will do the job just fine. To do that, you will need to copy the graphs made in the WeCMS_plotter folder and __paste them as shortcuts__ to Dropbox. Then you need to create a public link for eatch graph (or set of graphs). Now you need to make a website for your project. I have created 2 websites. [One from scratch]() and [one with Weebly's templates](http://wecmsplotter.weebly.com/) 
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
