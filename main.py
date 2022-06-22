from PIL import Image
import numpy as np
import sys

file_in = repr(sys.stdin[0])
file_out = repr(sys.stdin[1])
comp = int(sys.stdin[2])

# file_in = r"C:\Users\huber\PycharmProjects\ImageToASCII\Test Folder In\Gardevoir.jpg"
# file_out = r"C:\Users\huber\PycharmProjects\ImageToASCII\Test Folder Out\Gardevoir_ASCII.txt"
# comp = 3

im = Image.open(file_in)
pix = im.load()

data_write = open(file_out, "w")
data = open(file_out)


def big_pix(pix, size, x, y):
    pix_sum = [0, 0, 0]
    for i in range(x, x + size):
        for n in range(y, y + size):
            pix_sum[0] += pix[x, y][0]
            pix_sum[1] += pix[x, y][1]
            pix_sum[2] += pix[x, y][2]
    pix_mean = np.array(pix_sum) // size ** 2
    return tuple(pix_mean)


# def ASCIIconversion(r, g, b):


for y in range(0, im.size[1], comp):
    image_row = []
    for x in range(0, im.size[0], comp):
        r = big_pix(pix, comp, x, y)[0]
        g = big_pix(pix, comp, x, y)[1]
        b = big_pix(pix, comp, x, y)[2]
        conv = int((r + g + b)) // 6
        pixel_ascii = chr(max(conv, 50))
        image_row.append(" " + str(pixel_ascii))
    data_write.write("".join(image_row) + "\n")

data.close()
