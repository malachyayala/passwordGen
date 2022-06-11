#!/usr/bin/env python3
import string
from random import choice
import random
import sys
import argparse

files = "words.txt"
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--words", type = int, help = "include WORDS words in the password (default=4)", default = 4)
parser.add_argument("-c", "--caps", type = int, help = "capitalize the first letter of CAPS random words (default=0)", default = 0)
parser.add_argument("-n", "--numbers", type = int, help = "insert NUMBERS random numbers in the password (default=0)", default = 0)
parser.add_argument("-s", "--symbols", type = int, help = "insert SYMBOLS random symbols in the password (default=0)", default = 0)
args = parser.parse_args()
lines = []
pword = []
finalPW = ""
symbolString = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
symbol = list(symbolString)

with open('words.txt') as f:
    lines = f.read().splitlines()
if args.words:
    if args.words <= 4:
        for i in range(4):
            pword.append(random.choice(lines))
    elif args.words > 4:
        for i in range(args.words):
            pword.append(random.choice(lines))
    finalPW = ''.join(pword)
if args.caps:
    listPW = list(finalPW)
    for i in range(args.caps):
        if (args.caps == args.words):
            listPW[i] = listPW[i].title()
        randomNum = random.randint(0, len(listPW))
        if randomNum == len(listPW):
            randomNum = randomNum - 1
        listPW[randomNum] = listPW[randomNum].title()
    finalPW = ''.join(listPW)
if args.numbers:
    numsPass = list(finalPW)
    for i in range(args.numbers):
        randInt = random.randint(0, 100)
        numsPass.insert(random.randint(0, len(numsPass)), randInt)
    stringNums = [str(int) for int in numsPass]
    finalPW = ''.join(stringNums)
if args.symbols:
    hasSyms = list(finalPW)
    for i in range(args.symbols):
        randChoice = random.choice(symbol)
        hasSyms.insert(random.randint(0, len(hasSyms)), randChoice)
    finalPW = ''.join(hasSyms)
print(finalPW)
