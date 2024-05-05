from machine import Pin, I2C
from SSD1306 import SSD1306_I2C
import array

##Display
WIDTH =128 
HEIGHT= 64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

while True:
    triangle = array.array('I', [10,10,10,30,30,20])
    oled.poly(0,0, triangle, 0, True)
    oled.show()
