from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Simple encryption: swap channels and apply a basic operation
    encrypted_pixels = pixels[:, :, ::-1] + key

    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Simple decryption: reverse the encryption process
    decrypted_pixels = pixels[:, :, ::-1] - key

    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    while True:

        print("\nImage Encryption/Decryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(image_path, output_path, key)
        elif choice == '2':
            image_path = input("Enter the path to the image to decrypt: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(image_path, output_path, key)
        elif choice == '3':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
