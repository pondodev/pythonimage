from sys import argv
from PIL import Image, ImageFilter

def main(arg):
    img = Image.open(arg)
    img = img.convert("RGB") # if it's got RGBA space, we need to flatten it to RGB so we can save as jpg
    r,g,b = img.split()
    r.save("red.jpg")
    g.save("green.jpg")
    b.save("blue.jpg")

if __name__ == '__main__':
    if len(argv) != 2:
        print('please enter a file name as an argument')
    else:
        main(argv[1])