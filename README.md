# unXored
XOR Encryption Decryptor

It can brute the key for decrypting some *one byte xor* and can decrypt *repeated xor* with its key.

## Installation

```
git clone https://github.com/brokenheartz/unXored.git
cd unXored
sudo pip3 install -r requirements.txt
./xor.py
```

## Usage

For decrypting one byte xor, you can type :

**./xor.py -s <encrypted string/file> -b**

For decrypting repeated xor, you can type:

**./xor.py -s <encrypted string/file> -r <xor key>**

For storing the output into a file, you can type:

**./xor.py -s <encrypted string/file> -b -f**

or

**./xor.py -s <encrypted string/file> -r <xor key> -f**
