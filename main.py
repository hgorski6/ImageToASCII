from PIL import Image
import numpy as np
import os
import sys

# Taking inputs from command line
file_in = sys.argv[1]
file_path_out = sys.argv[2]

# This would control the compression rate of the output ASCII image
# (so "comp = 2" would mean the width and height of the image would be roughly 2 times smaller),
# however the function has been deprecated to issues.
# comp = sys.argv[3]

comp = 1

im = Image.open(file_in)
pix = im.load()

# the pathname of the output file, along with the file name
file_out = file_path_out + "\\" + os.path.basename(im.filename).replace("." + im.format.lower(), "") + r"_ASCII.txt"

data_write = open(file_out, "w")
data = open(file_out)


# The logic behind compressing the output ASCII image is to divide the image into grid of "comp x comp" squares
# and take the mean rgb values as the rgb value of each square, and then convert each such square to ASCII character
# as if we were handling an image - this is what this function would calculate.
# Unfortunately, the image looks worse with increase in comp, turning into a square of
# non-renderable character for comp = 4. However it still works for no compression (so comp = 1),
# therefore I decided to leave this code in
def big_pix(x, y):
    pix_sum = np.array([0, 0, 0])
    for i in range(x, x + comp):
        for k in range(y, y + comp):
            pix_sum = + np.array(pix[min(i, im.height - 1), min(k, im.width - 1)])
    pix_mean = pix_sum / comp ** 2
    return pix_mean


# This code converts each pixel to an ASCII character using char function,
# by calculating their mean then rounding it down.
# Afterwards, it compiles them in a list, which gets appended to the final file.
# This action is repeated for each row of the image.
# If one of the rgb values is greater than 85 however, is has to be scaled down by 85/255.
# This guarantees the final number, conv, can be converted to an ASCII character.
# Moreover, it also improves the quality of the final picture
for y in range(0, im.size[1], comp):
    image_row = []
    for x in range(0, im.size[0], comp):
        final_col = np.array([0, 0, 0])
        i = 0
        for col in big_pix(x, y):
            squeeze = col * int(col > 85) * (85 / 255)
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
