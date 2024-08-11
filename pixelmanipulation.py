from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)
    encrypted_pixels = pixels ^ key
    encrypted_img = Image.fromarray(encrypted_pixels)
    encrypted_img.save(output_path)

def decrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)
    decrypted_pixels = pixels ^ key
    decrypted_img = Image.fromarray(decrypted_pixels)
    decrypted_img.save(output_path)

def main():
    while True:
        mode = input("Would you like to 'encrypt' or 'decrypt' an image? ").lower()
        image_path = input("Enter the path to the image: ")
        output_path = input("Enter the output path for the processed image: ")
        key = int(input("Enter a key (integer value) for the encryption/decryption: "))

        if mode == 'encrypt':
            encrypt_image(image_path, output_path, key)
            print(f"Image encrypted and saved to {output_path}")
        elif mode == 'decrypt':
            decrypt_image(image_path, output_path, key)
            print(f"Image decrypted and saved to {output_path}")
        else:
            print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")

        again = input("Would you like to process another image? (yes/no): ").lower()
        if again != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
