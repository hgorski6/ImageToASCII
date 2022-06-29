from PIL import Image
import numpy as np
import os
import sys

# Taking inputs from command line
# The third parameter controls the compression rate of the output ASCII image
# (so "comp = 2" would mean the width and height of the image would be roughly 2 times smaller).
file_in = sys.argv[1]
file_path_out = sys.argv[2]
comp = int(sys.argv[3])

# This handles the compression of the image while making sure the ratio is maintained
im_input = Image.open(file_in)
width_comp = im_input.size[1] // comp
im_input_ratio = im_input.size[0]/im_input.size[1]
height_comp = int(im_input_ratio*width_comp)
im = im_input.resize((height_comp, width_comp))
pix = im.load()

# the pathname of the output file, along with the file name
file_out = file_path_out + "\\" + os.path.basename(im_input.filename).replace("." + im_input.format.lower(), "") \
           + r"_ASCII.txt"

data_write = open(file_out, "w")
data = open(file_out)

# This code converts each pixel to an ASCII character using char function,
# by calculating their mean then rounding it down.
# Afterwards, it compiles them in a list, which gets appended to the final file.
# This action is repeated for each row of the image.
# If one of the rgb values is greater than 85 however, is has to be scaled down by 85/255.
# This guarantees the final number, conv, can be converted to an ASCII character.
# Moreover, it also improves the quality of the final picture
for y in range(0, im.size[1]):
    image_row = []
    for x in range(0, im.size[0]):
        final_col = np.array([0, 0, 0])
        i = 0
        for col in pix[x, y]:
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
