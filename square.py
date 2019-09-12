from sys import argv
from PIL import Image, ImageFilter
from random import randrange

def main(arg):
    img = Image.open(arg)
    x = img.size[0]
    y = img.size[1]
    # get a random slice from the image
    rootx = randrange(0, x)
    rooty = randrange(0, y)
    nextx = randrange(rootx, x)
    nexty = randrange(rooty, y)
    box = (rootx, rooty, nextx, nexty)

    # crop and save
    img = img.crop(box)
    img = img.convert("RGB") # if it's got RGBA space, we need to flatten it to RGB so we can save as jpg
    img.save("test.jpg")

if __name__ == '__main__':
    if len(argv) != 2:
        print('please enter a file name as an argument')
    else:
        main(argv[1])