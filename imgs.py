import os
import glob

imgs = glob.glob('LX*/* *.jpg')

for img in imgs:
    os.rename(img, img.replace(' ', ''))
