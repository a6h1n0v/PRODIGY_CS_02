# Pixel Manipulation Image Encryption Tool

This repository contains a simple image encryption and decryption tool built using Python. The tool manipulates image pixels to provide basic encryption, allowing users to secure and restore images using a specified key.

## Features

- **Encrypt Images**: Applies XOR-based pixel manipulation to encrypt the image.
- **Decrypt Images**: Reverses the encryption to restore the original image.
- **User-Friendly**: Command-line interface that allows users to encrypt/decrypt multiple images in one session.

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- **Pillow**: Used for image processing.
- **NumPy**: Used for pixel manipulation.

You can install these dependencies using `pip`:

```bash
pip install pillow numpy
