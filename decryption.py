from chaosmaps import *

def make_binary_message(binary_string):
    secret = ''
    for i in range(0, len(binary_string),8):
        chunk = binary_string[i:i+8]
        chunk_to_num = int(chunk, 2)
        secret +=chr(chunk_to_num)
    return secret

def decrypt_secret(imagepath):
    secret_length = 80  # 10 characters * 8 bits per character

    #reversed steps
    noisy_secret = extract_noise(imagepath, secret_length)
    noisy_ts = generate_time_series(secret_length)
    decrypted_secret = apply_noise(noisy_secret, noisy_ts)
    original_message = make_binary_message(decrypted_secret)
    original_message = original_message[:10]

    return original_message.strip()