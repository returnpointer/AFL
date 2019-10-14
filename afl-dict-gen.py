#!/usr/bin/python

import argparse
import subprocess

parser = argparse.ArgumentParser(description='AFL magic word dictionary generator')

parser.add_argument("-i", default='.', type=str, help='Input directory path')
parser.add_argument("-o", default='.', type=str, help='Output directory path')

args = parser.parse_args()

print("Input executables dir: %s", args.i)
print("Output dictionary dir: %s", args.o)

str = subprocess.check_output(["find", args.i, "-executable", "-type", "f"])

execs = str.split('\n')

for f in execs:
    fptr = open(f+".od", "w")
    fptr.write(subprocess.check_output(["objdump", "-d", f]))
    fptr.close()