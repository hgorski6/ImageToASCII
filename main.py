from PIL import Image
import numpy as np
import sys

# file_in = repr(sys.argv[1])
# file_out = repr(sys.argv[2])
# comp = int(sys.argv[3])
#
# print(file_in)
# print(file_out)
# print(comp)

file_in = r"C:\Users\huber\PycharmProjects\ImageToASCII\Test Folder In\Gardevoir.jpg"
file_out = r"C:\Users\huber\PycharmProjects\ImageToASCII\Test Folder Out\Gardevoir_ASCII.txt"
comp = 1

im = Image.open(file_in)
pix = im.load()

data_write = open(file_out, "w")
data = open(file_out)

def big_pix(pix, size, x, y):
    pix_sum = np.array([0, 0, 0])
    for i in range(x, x + size):
        for k in range(y, y + size):
            pix_sum = + np.array(pix[min(i, im.height - 1), min(k, im.width - 1)])
    pix_mean = pix_sum / size ** 2
    return pix_mean


# def ASCIIconversion(r, g, b):


for y in range(0, im.size[1], comp):
    image_row = []
    for x in range(0, im.size[0], comp):
        conv = 50 + int(sum(big_pix(pix, comp, x, y)) // 6)
        pixel_ascii = chr(conv)
        if conv >= 86:
            pixel_ascii = "."
        # if conv in list(range(7, 14)) or conv in range(30, 34):
        #     pixel_ascii = chr(conv + 7)
        image_row.append(" " + str(pixel_ascii))
    ascii_line = "".join(image_row) + "\n"
    data_write.write(ascii_line)

data.close()
