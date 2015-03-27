import time
time.sleep(1)
import simpletables
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=24)

width = disp.width
height = disp.height
font = ImageFont.truetype('font.ttf', 30)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()


while True:
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,2,2), outline=255, fill=255)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((2,2), simpletables.get("Gyro", "load..."),  font=font, fill=255)
    
    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(0.001)

