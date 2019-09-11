from sys import argv
from PIL import Image, ImageFilter

def main(arg):
    img = Image.open(arg)
    x = img.size[0]
    y = img.size[1]
    minlen = min(x, y)
    box = (0, 0, minlen, minlen) # tuple that defines area we wish to crop
    img = img.crop(box)
    img = img.convert("RGB") # if it's got RGBA space, we need to flatten it to RGB so we can save as jpg
    img.save("test.jpg")

if __name__ == '__main__':
    if len(argv) != 2:
        print('please enter a file name as an argument')
    else:
        main(argv[1])