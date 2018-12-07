# General
Scope for the project of Sistemas Microprocessados - 2018.2  
Professor: Ricardo Jardel

# Team:
Luiky Magno Luz Vasconcelos (397877)  
Luan Pereira de Lima Brasil (397743)

# Brief Description of the project:
In order to avoid car crashes and worse accidents due to drunk people driving theirs cars, we propose a device to detect the driver's alcohol levels. The ideia is to identify whether the driver is drunk or not. With that in mind, companies, for example, may use it for monitoring of their driver employees. So, to do that, a system of data transmition is made to get information from the sensor, passing through a ESP8266-01 Wi-Fi Module, which sends data to an online platform (ThingSpeak) and send it to a Telegram Bot. In order to accomplish that, a code in C is used to control the data management from the sensor to the Cortex M0, which transmit it to the Wi-Fi module. The ESP8266-01, then, connects to the Wi-Fi (previously configurated in the code) via the 'AT' commands to ThingSpeak. This platform is responsible for receiving the information from the ESP8266 and passing it to the Bot using a code in Python (using Telepot library). Therefore, if the driver is drunk, the system will handle it and some responsible connected to the Bot can be informed about the situation. A limitation of this project, though, is that the device has to be always connected to the Wi-Fi to work properly. Besides, as the sensor used (MQ3) is developed for academic practices, it doesn't have a fully trustable precision. On the other hand, the web transmition is and advantage when it comes to long distances transmitions, making possible for anyone with access to the bot to have a control of the driver's driving condition from pratically anywhere in the world!
