# EXPO9_LeitzMicroscope

## Project overview

This project focuses on the automation of a Leitz Metallux II microscope as part of the EXPO projects at Fontys University of Applied Sciences.

The goal is to develop a system that combines mechanical movement, electronics, software, and control theory to automate scanning and image acquisition.

the software aims to process individual microscope images and combine them into a larger overview of the scanned area for the user to inspect.

# Project Modules
The project is designed as a modular system, with different components responsible for specific microscope automation tasks.

# Current Features
## Image Slicer

the image slicer is for testing use cases. it divides a larger image into smaller tiles.

- configurable tile sizes and overlap.
- saves tiles with identifiers in their filename (row & column).
- generates test images for the stitching algorithms.

## Grid-based Image stitcher

the grid stitcher combines tiles based on their row and column identifiers
- reads tile coordinates
- calculates tile position on the overlap
- places tiles onto a shared canvas
- saves the resulting image as an overview

**current limitation:** the tiles are placed using a predetermined grid position. The program does not correct for positioning error or blends overlapping regions.

## Automatic Image stitcher
an alternative stitching method is also implemented that solely relies on the built-in OpenCV stitching capabilities to attempt to align the images automatically.

this method can be used to compare the grid based approach.

## Requirements
the image processing scripts use Python with the following libraries

- Python 3
- OpenCV (opencv-python)
- NumPy

## Current status {Image stitcher}
the image slicer and basic stitching have been implemented and tested using sample images. The software is still under development.

### known limitations
- grid stitcher assumes tiles that follow a regular grid
- grid stitcher is heavily dependent on correctly formatted indentifiers
- real stitching using microscope images have not been validated yet

# Contributers
Zachariah van Tongeren (MC4A) - Image stitching & image slicer 
