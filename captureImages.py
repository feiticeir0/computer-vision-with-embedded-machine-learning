"""
    This script will take 50 images
    with a 96x96 resolution
    then, will convert them to grayscale

    Edge Impulse Computer Vision with Embedded Machine Learning

    Some code was taken from the Documentation for the PiCamera,
    here:
    https://picamera.readthedocs.io/en/latest/recipes2.html

"""

import time
# Picamera functions
import picamera
import glob

#converting to grayscale
from PIL import Image, ImageOps

#images location
location = 'usbpen/'

#how many pictures to take
howmany = 50

# take that many pictures
with picamera.PiCamera() as camera:
    camera.resolution = (96,96)
    camera.framerate = 30
    camera.start_preview()
    #give some warm up and adjust stuff - focus
    time.sleep(10)
    start = time.time()
    camera.capture_sequence([
        location + '%02d.bmp' % i
        for i in range(howmany)
        ], use_video_port=True)
    finish = time.time()

print ('Captured %d frames at %.2ffps' % (howmany, howmany / (finish - start)))

print ('Converting to grayscale')

imagesList = glob.glob(location + '*.bmp')

for image in imagesList:
    img_org = Image.open(image)
    img_gray = ImageOps.grayscale(img_org)
    img_gray.save(image)

print ('Images converted to grayscale')

