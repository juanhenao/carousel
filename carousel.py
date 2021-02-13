#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
imagesDir = './images'
libDir = './lib'
if os.path.exists(libDir):
    sys.path.append(libDir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

img_names = ["2in13", "2in13_2"]

def load_image(img):
    logging.info("Printing image " + img + '.bmp')
    image = Image.open(os.path.join(imagesDir, img + '.bmp'))
    epd.display(epd.getbuffer(image))
    time.sleep(5)


try:
    logging.info("Image Carousel")
    
    epd = epd2in13_V2.EPD()
    logging.info("Init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    while True:
        [load_image(img) for img in img_names]
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
