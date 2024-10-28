-虛擬環境安裝-  

*查詢: python --version  
  
*python下載:
Note that Python 3.10.10 cannot be used on Windows 7 or earlier.  
[Download Windows installer (64-bit)](https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe)  

1->環境變數  
C:\Users\P101\AppData\Local\Programs\Python\Python310\Scripts\  
C:\Users\P101\AppData\Local\Programs\Python\Python310\  
  
2->安裝virtualenv  
pip install virtualenv  
virtualenv 取一個名稱  
  
3->啟動  
到虛擬環境Scripts目錄中啟動  
activate  

------------------------------------------------------------------------------  
-pi4 with dht22-  

https://www.raspberrypi.com/software/  
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html  
https://www.realvnc.com/en/connect/download/viewer/?lai_sr=0-4&lai_sl=l  
https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-4.png.webp?ssl=1  

*指令:    
sudo apt update  
sudo apt upgrade  
sudo raspi-config  
ifconfig  
sudo reboot  

*建立Virtualenv:  
python -m venv myenv  
source myenv/bin/activate  

*設定DHT11,DHT22:  
Python Setup  
https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup  
Installing the CircuitPython-DHT Library  
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi  

----------------------------------------------------------------------------------------------------------------------  
-MQTT Pi4-  
sudo apt-get install mosquitto mosquitto-clients  
sudo systemctl enable mosquitto.service  
sudo nano /etc/mosquitto/mosquitto.conf  
listener 1883  
allow_anonymous true  
sudo reboot  
ifconfig  
pip install 'paho-mqtt<2.0.0'  
pip install rpi.gpio  
git clone https://github.com/miyachun/raspberry-pi4-MQTT  


-------------------------------------------------------------------------------------------------------------------------  

-其它相關-  
virtualenv->virtualenv -p python3.10 XXX  
RUNOOB->https://www.runoob.com/python3/python3-tutorial.html  
FLASK->[https://flask.palletsprojects.com/en/3.0.x/installation/#python-version](https://flask.palletsprojects.com/en/3.0.x/)  
Line Developer->https://developers.line.biz/en/  
Line Flex Messages->https://developers.line.biz/en/docs/messaging-api/using-flex-messages/  
STEAM 教育學習網->https://steam.oxxostudio.tw/category/python/spider/yahoo-stock.html  
氣象資料開放平臺->https://opendata.cwa.gov.tw  
python軟體->https://www.python.org/downloads/windows/  
影片播放軟體->https://potplayer.daum.net/  
Ngrok軟體->https://ngrok.com/  
Weather API->https://www.weatherapi.com  
https://github.com/weatherapicom/python  
