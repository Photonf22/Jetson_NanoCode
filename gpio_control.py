#!/usr/bin/env python

# Copyright (c) 2019-2022, NVIDIA CORPORATION. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import Jetson.GPIO as GPIO
import time

# Pin Definitions
#output_pin = 18  # BCM pin 18, BOARD pin 12
#this is just a small code made in python to control the Jetson nano GPIO
# note this only works with python2.7
# note GPIO is running at 3.3v output which is enough to send a take frame
# signal to basler camera. Do not exceed this current else you will damage
# camera components I/O can only receieve less than 5V and registers a high
# at anything above 1.8V
def main():
    # Pin Setup:
    GPIO.setmode(GPIO.TEGRA_SOC)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup('SPI1_MOSI', GPIO.OUT, initial=GPIO.HIGH)
    

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            time.sleep(1) # toggle every second for Basler Camera shot
            # Toggle the output every second
            curr_value=GPIO.HIGH    
            print("Outputting {} to pin {}".format(curr_value, 'SPI_MOSI'))
            GPIO.output('SPI1_MOSI', GPIO.HIGH)
            curr_value ^= GPIO.HIGH
            GPIO.output('SPI1_MOSI',GPIO.LOW)
            print("Outputting {} to pin {}".format(curr_value, 'SPI_MOSI'))
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
