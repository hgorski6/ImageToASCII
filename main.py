from PIL import Image
import sys

# file_in = sys.stdin[0]
# file_out = sys.stdin[1]

file_in = r"C:\Users\huber\PycharmProjects\ImageToASCII\Test Folder In\Gardevoir.jpg"
file_out = r"C:\Users\huber\PycharmProjects\ImageToASCII\Test Folder Out\Gardevoir_ASCII.txt"

im = Image.open(file_in)
pix = im.load()

data_write = open(file_out, "w")
data = open(file_out)

for y in range(im.size[1]):
    image_row = []
    for x in range(im.size[0]):
        pixel_ascii = chr(int((pix[x, y][0] + pix[x, y][1] + pix[x, y][2]) / 6))
        image_row.append(" " + str(pixel_ascii))
    data_write.write("".join(image_row) + "\n")

data.close()
