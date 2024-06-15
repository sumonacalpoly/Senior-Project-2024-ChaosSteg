import numpy as np
from PIL import Image

def logistic_map(x,r):
    return r * x * (1-x)

def generate_time_series(size):
    x = 0.5 # common seed
    time_series = [x]

    for _ in range(size - 1):
        x = logistic_map(x,5.2) # r can be chosen to be any num
        x = (x- np.floor(x)) #limit between 0 and 1
        time_series.append(x)

    return np.array(time_series)

def apply_noise(binary_secret, noisy_time_series):
    blist = list(binary_secret)
    binary_length = len(blist)

    for i in range (binary_length):
        bit = int(blist[i])
        magic_num = noisy_time_series[i % len(noisy_time_series)]
        bit = bit ^ int(magic_num * 2) #xor
        blist[i] = str(bit)
    
    return "".join(blist)

def extract_noise(imagepath, size):
    image = Image.open(imagepath)
    width, height = image.size
    noisy_secret = ''
    n = 0

    for i in range(0, width):
        for j in range(0, height):
            pixel = list(image.getpixel((i, j)))
            for val in range(0, 3):
                if n < size:
                    noisy_secret += str(pixel[val] & 1)
                    n += 1
                else:
                    break
            if n >= size:
                break
        if n >= size:
            break

    return noisy_secret.zfill(size)