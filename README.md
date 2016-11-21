<h1 align="center">Roland P10 FP</h1>
<h3 align="center">File preperation script for the Roland's P-10 Image Converter Lite</h3>
<h3 align="center">
  <img src="http://i.imgur.com/isx076I.jpg"/>
</h3>

current formats
========
- input: .mp4/.mov/.avi (* this will be expanded in the future)
- output: .mpg

requirements
========
- Python (https://www.python.org/)
- ffmpeg (http://ffmpeg.org/)
- Roland P-10 Image Converter Lite (http://proav.roland.com/products/p-10/downloads/)

how to use
========
1. First, place the files you wish to convert in the folder labeled "raw-videos"
2. Open the terminal and change the directory to this folder (rolandp10fp)
3. Run the script by typing "python rolandp10fp.py". Automatically a new folder named "converted" will be created and filled with videos with the extension ".mpg".
4. You're done! All the files in the folder named "converted" are now properly encoded and can be converted correctly using the "Roland P-10 Image Converter Lite" application for the Roland P-10 video sampler