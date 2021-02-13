#!/bin/bash

sudo apt update
sudo apt install python3-pip
sudo apt install python3-pil
sudo apt install python3-numpy


pip3 install RPi.GPIO
pip3 install spidev
pip3 install Pillow

#Enable spi interface in raspberry config