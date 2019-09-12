from sys import argv
from PIL import Image, ImageFilter
from random import randrange

# get a small subsection of the given image
def getSlice(img):
    x, y = img.size
    ytop = randrange(0, y)
    ybottom = randrange(ytop, y)
    box = (0, ytop, x, ybottom)

    return (img.crop(box), box)

# wrap the given image around
def roll(img, delta):
    x, y = img.size

    delta = delta % x
    if delta == 0: return img

    part1 = img.crop((0, 0, delta, y))
    part2 = img.crop((delta, 0, x, y))
    img.paste(part2, (0, 0, x - delta, y))
    img.paste(part1, (x - delta, 0, x, y))

    return img

# move two colour channels in opposite directions
def channelShift(img, delta):
    r,g,b = img.split()
    r = roll(r, delta)
    g = roll(g, -delta)
    return Image.merge("RGB", (r, g, b))

def main(arg):
    img = Image.open(arg)

    # shift slices around
    slices = randrange(10, 50)
    for i in range(slices):
        temp, box = getSlice(img)
        temp = roll(temp, randrange(-10, 10))
        img.paste(temp, box)

    # give it that spicy channel shifting touch
    img = img.convert("RGB")
    img = channelShift(img, randrange(-10, 10))

    img.save("test.jpg")

if __name__ == '__main__':
    if len(argv) != 2:
        print('please enter a file name as an argument')
    else:
        main(argv[1])