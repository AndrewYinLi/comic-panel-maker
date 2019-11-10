from PIL import Image
import sys
from tqdm import tqdm

img_init = Image.open(sys.argv[1])
w_out, h_out = img_init.size
w_out *= (len(sys.argv)-1)
img_out = Image.new("RGB", (w_out, h_out))

w_pointer = 0

for i in tqdm(range (1, len(sys.argv)), desc="all"):
    img_cur = Image.open(sys.argv[i])
    px_cur = list(img_cur.getdata())
    w_cur, h_cur = img_cur.size

    for x in tqdm(range(0, w_cur), desc="indie"):
        for y in range(0, h_cur):
            if x < 10: # draws borders
                 img_out.putpixel((x+w_pointer,y), (0,0,0))
            else:
                color_xy = img_cur.getpixel((x, y))
                img_out.putpixel((x+w_pointer,y), color_xy)

    w_pointer += w_cur

img_out.save("out.png")