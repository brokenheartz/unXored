#!/usr/bin/python3

from argparse import ArgumentParser
from colorama import *
from sys import argv
from itertools import cycle # repeating characer of a string
import os

init( autoreset = True )

class XorEnc() :

    _plaintext = {}

    def __init__(self, enc, isonebyte = True, key = ""):

        self._encryption = enc
        self._string = ""
        self._onebyte = isonebyte
        self._key = key # for repeated xor
        self.decrypt()

    def decrypt(self):

        if self._onebyte: # one byte xor

            for key in range(0, 256):
                for char in self._encryption:
                    self._string += chr(ord(char) ^ key)
                XorEnc._plaintext[key] = self._string
                self._string = ""

        else : # repeated xor

            zipping = list(zip(self._encryption, cycle(self._key)))

            for cipher, key  in zipping:

                self._string += chr(ord(cipher) ^ ord(key))

            XorEnc._plaintext[self._key] = self._string

    def _return(self):
        return XorEnc._plaintext

class color():

    BOLD = Style.BRIGHT
    NORMAL = Style.NORMAL
    DIM = Style.DIM

    RED = Fore.RED
    BLACK = Fore.BLACK
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE

def banner():
    print(color.BOLD + color.RED + """
              )
           ( /(              (
   (       )\())    (     (  )\ )
  ))\  (  ((_)\  (  )(   ))\(()/(
 /((_) )\ )_((_) )\(()\ /((_)((_))"""
 + color.WHITE + """
(_))( _(_/( \/ /((_)((_|_))  _| |
| || | ' \)>  </ _ \ '_/ -_) _` |
\\\_,_|_||_/_/\_\___/_| \___\__,_|
""" + "\t\t\t[" + color.BLUE +" Xor Decryptor " + color.WHITE + "]")

def usage():
    print()
    print(color.YELLOW + "[+]" + color.GREEN + " {} --string <encrypted string> -r <xor key>".format(argv[0]))
    print(color.YELLOW + "[+]" + color.GREEN + " {} --string <encrypted string> -b".format(argv[0]))
    print(color.YELLOW + "[+]" + color.GREEN + " {} --string <encrypted string> (-r/-b) -f filename.ext".format(argv[0]))
    print(color.YELLOW + "[+]" + color.GREEN + " {} --help / -h".format(argv[0]))

def store_output(isonebyte = True):
    global xorenc

    try:
        os.mkdir("xor_output")
        os.chmod("xor_output", 0o777)
    except Exception:
        pass

    for key, plaintext in xorenc._return().items():

        if isonebyte == True:
            try:
                output = open("xor_output/bxor%d.txt" % key, "w")
                output.write("{} : {}".format(key, plaintext))
                print(color.YELLOW + "[+]" + color.GREEN + " created {}".format("bxor%d.txt" % key))
            except Exception:
                pass
            else:
                output.close()
        else:
            try:
                output = open("xor_output/rxor_{}.txt".format(key), "w")
                output.write("{} : {}".format(key, plaintext))
                print(color.YELLOW + "[+]" + color.GREEN + " crated {}".format("rxor_{}.txt".format(key)))
            except Exception:
                pass
            else:
                output.close()

def display_output():
    global xorenc
    for key, plaintext in xorenc._return().items():
        print(color.YELLOW + "[+]" + color.GREEN + " {} : {}".format(key, plaintext))

banner()

input = ArgumentParser( description = "A tool for decrypt XOR encryption" )
group = input.add_mutually_exclusive_group()

group.add_argument("-b", "--basic", help = "decrypt basic / one byte xor", action = "store_true")
group.add_argument("-r", "--repeated", help = "decrypt repeated xor", default = None)
input.add_argument("-s", "--string", help = "encrypted string / file")
input.add_argument("-f", "--file", help = "store input into a file", action = "store_true")
input.add_argument("-v", "--version", action = "version", version = color.YELLOW + "[+]" + color.GREEN + " unXored v0.1", help = "show the version of this program")

args = input.parse_args()

if not args.string:
    usage()
else:

    if args.basic:
        if os.path.isfile(args.string):
            readf = open(args.string, "r")
            xorenc = XorEnc(readf.read())
            readf.close()
        else:
            xorenc = XorEnc(args.string)

        if args.file:
            store_output()
        else:
            display_output()
    elif args.repeated:
        if os.path.isfile(args.string):
            readf = open(args.string, "r")
            xorenc = XorEnc(readf.read(), False, args.repeated)
            readf.close()
        else:
            xorenc = XorEnc(args.string, False, args.repeated)

        if args.file:
            store_output(False)
        else:
            display_output()
