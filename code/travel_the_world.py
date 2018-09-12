# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import time
import pygame
import lcddriver
import time, subprocess, datetime
from datetime import timedelta




def weltuhr(x):
 global ortszeit
 global uhrzeit
 ortszeit = datetime.datetime.utcnow() + timedelta(hours = x)
 uhrzeit = ortszeit.strftime("%H:%M   %d.%m.%y")




import Adafruit_MPR121.MPR121 as MPR121

# Thanks to Scott Garner & BeetBox!
# https://github.com/scottgarner/BeetBox/

print 'Travel the World - Scoutlab 2017'
lcd = lcddriver.lcd()
lcd.lcd_clear()

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# Alternatively, specify a custom I2C address such as 0x5B (ADDR tied to 3.3V),
# 0x5C (ADDR tied to SDA), or 0x5D (ADDR tied to SCL).
#cap.begin(address=0x5B)

# Also you can specify an optional I2C bus with the bus keyword parameter.
#cap.begin(busnum=1)

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()


SOUND_MAPPING = {
   0: '/home/pi/travel_the_world/sound/usa.wav',
   1: '/home/pi/travel_the_world/sound/australien.wav',
   2: '/home/pi/travel_the_world/sound/brasilien.wav',
   3: '/home/pi/travel_the_world/sound/groenland.wav',
   4: '/home/pi/travel_the_world/sound/indien.wav',
   5: '/home/pi/travel_the_world/sound/mexiko.wav',
   6: '/home/pi/travel_the_world/sound/russland.wav',
   7: '/home/pi/travel_the_world/sound/senegal.wav',
   8: '/home/pi/travel_the_world/sound/suedafrika.wav',
   9: '/home/pi/travel_the_world/sound/thailand.wav',
   10: '/home/pi/travel_the_world/sound/usa.wav',
   11: '/home/pi/travel_the_world/sound/deutschland.wav',
 }

sounds = [0,0,0,0,0,0,0,0,0,0,0,0]




for key,soundfile in SOUND_MAPPING.iteritems():
        sounds[key] =  pygame.mixer.Sound(soundfile)
        sounds[key].set_volume(1);

# Main loop to print a message every time a pin is touched.
print('Press Ctrl-C to quit.')
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    # Check each pin's last and current state to see if it was pressed or released.
    #
    #
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
           if i == 0:
	     pygame.quit()
             pygame.init()
	     stadt = 'Washington DC    '
             lcd.lcd_display_string(('%s' % stadt),1)
	     weltuhr(-5)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 1:
	     pygame.quit()
             pygame.init()
	     stadt = 'Canberra        '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(10)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 2:
	     pygame.quit()
             pygame.init()
	     stadt = 'Brasilia      '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(-3)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 3:
	     pygame.quit()
             pygame.init()
	     stadt = 'Nuuk            '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(-3)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 4:
	     pygame.quit()
             pygame.init()
	     stadt = 'Neu Delhi       '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(5.5)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 5:
	     pygame.quit()
             pygame.init()
	     stadt = 'Mexiko City    '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(-6)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 6:
	     pygame.quit()
             pygame.init()
	     stadt = 'Moskau          '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(2)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 7:
	     pygame.quit()
             pygame.init()
	     stadt = 'Dakar           '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(-1)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 8:
	     pygame.quit()
             pygame.init()
	     stadt = 'Kapstadt        '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(2)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 9:
	     pygame.quit()
             pygame.init()
	     stadt = 'Bangkok         '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(6)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 10:
	     pygame.quit()
             pygame.init()
	     stadt = 'Juneau          '
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(-9)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
	   if i == 11:
             stadt = 'Berlin          '
             pygame.quit()
             pygame.init()
             lcd.lcd_display_string(('%s' % stadt),1)
             weltuhr(1)
             lcd.lcd_display_string(('%s' % uhrzeit), 2)
 	   if (sounds[i]):
              sounds[i].play()
        
    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    
