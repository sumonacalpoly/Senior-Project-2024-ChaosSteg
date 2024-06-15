import os
import numpy as np
from PIL import Image
import random
import shutil
import random

#UNECESSARY NOW

def logistic_map(x, r):
    return r * x * (1 - x)

def generate_time_series(size, r=3.99, seed=0.5):
    x = seed
    time_series = [x]
    for _ in range(size - 1):
        x = logistic_map(x, r)
        x = (x - np.floor(x))
        time_series.append(x)
    return np.array(time_series)

def apply_noise(binary_secret, noisy_time_series):
    blist = list(binary_secret)
    binary_length = len(blist)
    for i in range(binary_length):
        bit = int(blist[i])
        magic_num = noisy_time_series[i % len(noisy_time_series)]
        bit = bit ^ int(magic_num * 2)
        blist[i] = str(bit)
    return "".join(blist)

def embed_secret(image_path, binary_secret, output_path):
    image = Image.open(image_path).convert('RGB')
    width, height = image.size
    img = np.array(image)

    secret_index = 0
    secret_len = len(binary_secret)

    for i in range(height):
        for j in range(width):
            for k in range(3):
                if secret_index < secret_len:
                    bit = int(binary_secret[secret_index])
                    img[i, j, k] = (img[i, j, k] & ~1) | bit
                    secret_index += 1

    stego_image = Image.fromarray(img)
    stego_image.save(output_path)

def certificate_to_binary(cert_path):
    with open(cert_path, "rb") as cert_file:
        cert_data = cert_file.read()
    return ''.join(format(byte, '08b') for byte in cert_data)

# dummy certificate (simulating unique certificate generation like from OPENSSL)
def generate_dummy_certificate(cert_id):
    cert_content = f"Certificate ID: {cert_id}\nIssuer: STEEDML\nNote: User Authneticated!\nValid From: 2024-01-01\nValid To: 2025-01-01\n"
    cert_path = f"dummy_cert_{cert_id}.pem"
    with open(cert_path, "w") as cert_file:
        cert_file.write(cert_content)
    return cert_path

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, filename in enumerate(os.listdir(input_folder)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            cert_path = generate_dummy_certificate(i)
            binary_certificate = certificate_to_binary(cert_path)            
            noisy_time_series = generate_time_series(len(binary_certificate))
            noisy_binary_certificate = apply_noise(binary_certificate, noisy_time_series)            
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            embed_secret(image_path, noisy_binary_certificate, output_path)
            print(f"Processed {filename}")

            os.remove(cert_path)

def main():
    train_input_folder = r""
    test_input_folder = r""
    train_output_folder = r""
    test_output_folder = r""

    process_folder(train_input_folder, train_output_folder)
    process_folder(test_input_folder, test_output_folder)

if __name__ == "__main__":
    main()
