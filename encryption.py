from chaosmaps import *
from lsb import lsb_stego

def make_message_binary(secret):
    binary = ''.join(format(ord(i), '08b') for i in secret)
    return binary

def encrypt_image(imagepath, secret):
    
    if len(secret) > 10:
        print("Message too long, truncating to 10 characters.")

    bsecret = make_message_binary(secret)
    print("binary secret is: ", bsecret)

    noisy_ts = generate_time_series(len(bsecret))
    nsecret = apply_noise(bsecret, noisy_ts)
    print("noisy secret is: ", nsecret)

    embedded_image= lsb_stego(imagepath, nsecret)
    print("Noisy secret embedded!", embedded_image)
    