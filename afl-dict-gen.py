#!/usr/bin/python

import argparse
import subprocess
import glob

parser = argparse.ArgumentParser(description='AFL magic word dictionary generator')

parser.add_argument("-i", default='.', type=str, help='Input directory path')
parser.add_argument("-o", default='.', type=str, help='Output directory path')

args = parser.parse_args()

print("Input executables dir: %s", args.i)
print("Output dictionary dir: %s", args.o)

str = subprocess.check_output(["find", args.i, "-executable", "-type", "f"])

execs = str.split('\n')

#for f in execs:
#    print(f)
#    fptr = open(f+".od", "w")
    
#    try:
#        fptr.write(subprocess.check_output(["objdump", "-d", f]))
#    except subprocess.CalledProcessError as e:
        # TODO: figure out how to
        # log exceptions to file.
        #logfile = open("log", "a")
        #logfile.write(e.output)
        #logfile.close()
#        print(e.output)
   
#    fptr.close()

objdumps = [f for f in glob.glob(args.i + "/*.od")]
#print(objdumps)

#for f in objdumps:
file = open(objdumps[0],"r")
for line in file:
    idx_b = line.find("cmp    $")
    if idx_b != -1:
        idx_m = line.find("$", idx_b)
        idx_e = line.find(",", idx_b)
        print(line[idx_m+1:idx_e])



