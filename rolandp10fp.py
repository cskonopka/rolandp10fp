import os
import time

def main():
    files = os.listdir("raw-videos")
    print files


    for f in files:
    	# print f.lower()[-3:]
        if f.lower()[-3:] == "mp4" or f.lower()[-3:] == "mov" or f.lower()[-3:] == "avi":
            print "processing", f
            process(f, f.lower()[-3:])

def process(f, d):
    inFile = f
    newFolder = "converted"
    os.system("mkdir " + newFolder)
    inFile = "raw-videos/" + f[:-3] + d
    outFile = newFolder + "/" + f[:-3] + "mpg"
    cmd = "ffmpeg -i {} -f mpeg {}".format(inFile, outFile)
    # print cmd
    os.popen(cmd)

main()