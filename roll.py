from sys import argv
from PIL import Image, ImageFilter
from random import randrange

def roll(img, delta):
    x, y = img.size

    delta = delta % x
    if delta == 0: return img

    part1 = img.crop((0, 0, delta, y))
    part2 = img.crop((delta, 0, x, y))
    img.paste(part2, (0, 0, x - delta, y))
    img.paste(part1, (x - delta, 0, x, y))

    return img

def main(arg):
    img = Image.open(arg)
    img = roll(img, 100)
    img.show()

if __name__ == '__main__':
    if len(argv) != 2:
        print('please enter a file name as an argument')
    else:
        main(argv[1])