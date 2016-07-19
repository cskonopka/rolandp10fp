import os
import time

def main():
    files = os.listdir("./")
    for f in files:
        if f.lower()[-3:] == "mp4":
            print "processing", f
            process(f)

def process(f):
    inFile = f
    outFile = f[:-3] + "mpg"
    cmd = "ffmpeg -i {} -f mpeg {}".format(inFile, outFile)
    os.popen(cmd)

main()