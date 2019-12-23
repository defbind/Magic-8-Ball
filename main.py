import random
from PIL import Image
import time

# Magic 8 ball
random = random.randint(0,2)
if random == 0:
    im = Image.open("/Users/alex/Desktop/8no.jpeg")
    im.show()
if random == 1:
    im1 = Image.open("/Users/alex/Desktop/8yes.jpeg")
    im1.show()
if random == 2:
    im2 = Image.open("/Users/alex/Desktop/8perhaps.jpeg")
    im2.show()