#!/usr/bin/python

import argparse
import subprocess

parser = argparse.ArgumentParser(description='AFL magic word dictionary generator')

parser.add_argument("-i", default='.', type=str, help='Input directory path')
parser.add_argument("-o", default='.', type=str, help='Output directory path')

args = parser.parse_args()

print("Input executables dir: %s", args.i)
print("Output dictionary dir: %s", args.o)

execs = subprocess.check_output(["find", args.i, "-executable -type f"])

for f in execs:
    print(f)