# vigener_Cipher
encryption and decryption with polyalphabetical cipher. you can use command line

# Caesar Cipher

## Description

This Python script provides functionalities for encrypting and decrypting text using the Caesar Cipher algorithm. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- **Encryption**: Convert plaintext into ciphertext using a specified key.
- **Decryption**: Reverse the encryption process to obtain the original plaintext.
- **Command-line Interface**: Easily interact with the script via command-line arguments.

## Usage

### Requirements

- Python 3.x
- colorama library (install via `pip install colorama`)

### Command-line Arguments

- `-k, --key`: Specify the encryption/decryption key.
- `-t, --text`: Choose whether the input is plaintext or ciphertext.
- `-w, --word`: Enter the text to be encrypted or decrypted.
- `-c, --cipher`: (Optional) Enter the ciphertext if decrypting.
- `-m, --mode`: Specify whether to encrypt (`enc`) or decrypt (`dec`) the text.

### Examples

#### Encryption

```bash
python caesar_cipher.py -k 3 -t plaintext -w "hello" -m enc
```
#### Decryption

```bash
python caesar_cipher.py -k 3 -t ciphertext -c "khoor" -m dec
