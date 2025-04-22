from machine import ADC, Pin
import time
import math
import json
import network
from umqtt.robust import MQTTClient
from config import WIFI_SSID, WIFI_PASS, MQTT_BROKER, MQTT_USER, MQTT_PASS





sound_sensor = ADC(Pin(32))
sound_sensor.atten(ADC.ATTN_11DB) 
sound_sensor.width(ADC.WIDTH_12BIT) 

V_REF = 3.3 
V_MIN = 0.002

led_wifi = Pin(2, Pin.OUT)
led_wifi.value(1)  
led_iot = Pin(12, Pin.OUT)
led_iot.value(1)   



wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASS)
while not wlan.isconnected():
    time.sleep(0.5)
led_wifi.value(0)  




mqtt = MQTTClient(client_id="",
                  server=MQTT_BROKER,
                  user=MQTT_USER,
                  password=MQTT_PASS)
mqtt.connect()
led_iot.value(0)
def read_sound():
    adc_value = sound_sensor.read()  
    
    V_out = adc_value * (V_REF / 4095)
    
    
    if V_out > V_MIN:  
        dB = 20 * math.log10(V_out / V_MIN)
        return dB
        print("Sound Level: {:.2f} dB".format(dB))

while True:
    data = {
    'sound' : read_sound(),
    'lat' : 13.710654,
    'lon' : 100.612193,
    }
    mqtt.publish('b6610545928/sound', json.dumps(data))
    print(data)
    time.sleep(300)
    
    
    
