#-*- coding:utf-8 -*-

from PIL import Image
import time

IMG = "./SYSU.png"
OUTPUT = "./HBD_SYSU.txt"
count = 0-1

# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# ascii_char = list("SYSUHAPPYBIRTHDAY")
ascii_char = list("SYSU")


def get_char(r,g,b,alpha = 256):
    global count
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    count+=1
    return ascii_char[count%len(ascii_char)]

if __name__ == '__main__':

    im = Image.open(IMG)
    WIDTH = 120
    HEIGHT = int(WIDTH * im.height / im.width)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    for i in range(HEIGHT):
        txt = ""
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
            txt += " "
        # txt += '\n'
        print(txt)
        time.sleep(0.03)
    # print(txt)
    
    #字符画输出到文件
    if not OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
