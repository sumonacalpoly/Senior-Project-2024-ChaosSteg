from encryption import encrypt_image
from decryption import decrypt_secret


def main():
    mode = input("Select Encryption [E] or Decryption [D] Mode: ")
    if mode == "E":
       image = input("Enter the path of the image file: ")
       secret = input("Enter the secret message: ")[:10]
       encrypted_image =  encrypt_image(image, secret)
       print("Image encrypted; Check output folder!", encrypted_image)

    elif mode == "D":
        image = input("Enter the path of the image file: ")
        decrypted_secret = decrypt_secret(image)
        print("decrypted message is:", decrypted_secret)
 
    else:
        raise Exception("Mode selection is incorrect!")


if __name__ == "__main__":
    main()