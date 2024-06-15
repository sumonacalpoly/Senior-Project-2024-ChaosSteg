from PIL import Image
import os

def lsb_stego(imagepath, noisy_secret):
    image = Image.open(imagepath)
    width,height = image.size
    n=0
    for i in range(0, width):
        for j in range(0, height):
            pixel = list(image.getpixel((i,j)))
            for val in range(0,3):
                if (n < len(noisy_secret)):
                    pixel[val] = pixel[val] & ~1 | int(noisy_secret[n]) #clear lsb and or new val
                    n+=1
            image.putpixel((i,j), tuple(pixel))
    title = os.path.basename(imagepath).replace('.png', '')
    newimagepath = os.path.join("output/", f"lsb-encrypted-{title}.png")
    image.save(newimagepath)
    return newimagepath