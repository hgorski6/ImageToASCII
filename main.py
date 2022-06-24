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


def big_pix(x, y):
    pix_sum = np.array([0, 0, 0])
    for i in range(x, x + comp):
        for k in range(y, y + comp):
            pix_sum = + np.array(pix[min(i, im.height - 1), min(k, im.width - 1)])
    pix_mean = pix_sum / comp ** 2
    return pix_mean


# pix_actual = map(big_pix, list(range(im.height)), list(range(im.width)))

for y in range(0, im.size[1], comp):
    image_row = []
    for x in range(0, im.size[0], comp):
        final_col = np.array([0, 0, 0])
        i = 0
        for col in big_pix(x, y):
            squeeze = col * int(col > 85) * (85 / 255)
            # forbidden = col * int(col in range(7, 14) or col == 32)
            final_col[i] = squeeze + col * int(col <= 85)
            i = + 1
        conv = int(sum(final_col) // 3)
        while conv in list(range(7, 14)) or conv == 32:
            conv = conv + 1
        pixel_ascii = chr(conv)
        image_row.append(" " + str(pixel_ascii))
    ascii_line = "".join(image_row) + "\n"
    data_write.write(ascii_line)

data.close()
