#!/bin/sh

## Disclaimer: This script is not yet tested!

## install v4l2
sudo apt-get install v4l2-tools libv4l-dev

## install opencv dependencies
# libav video input/output development libraries
sudo apt-get install libavformat-dev libavutil-dev libswscale-dev

# OpenGL development libraries (to allow creating graphical windows)
sudo apt-get install libglew-dev

# GTK development libraries (to allow creating graphical windows)
sudo apt-get install libgtk2.0-dev

# Install the OpenCV python
# sudo apt-get install python-opencv


## install opencv
sudo apt-get install python3-opencv

# # if that version isn't recent enough you can install from source
# tempdir=$(mktemp)
# cd tempdir
# wget https://github.com/opencv/opencv/archive/3.4.1.zip
# unzip opencv-3.4.1.zip
# cd opencv-3.4.1
# mkdir build && cd build
# sudo make -j$((`nproc`-1)) install

# [compiler]
# sudo apt-get install build-essential
#[required] 
# sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
#[optional]
# sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# optional
# sudo apt install ffmpeg 




# copy the systemd service to the right directory
# sudo ln
