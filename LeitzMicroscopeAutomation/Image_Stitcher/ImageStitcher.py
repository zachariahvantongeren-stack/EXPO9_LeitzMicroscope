import cv2
from pathlib import Path
import numpy as np
import re

def stitch_images(input_folder, output_folder):
    print("=====STARTING STITCHING=====")

    input_folder = Path(input_folder)
    output_folder = Path(output_folder)

    image_files = list(input_folder.glob("*.jpg")) #find all jpg files belonging to the scan
    
    images = []

    #for loop to read all the files
    for image_file in image_files:

        image = cv2.imread(str(image_file))

        if image is not None:
            images.append(image)
    
    stitcher = cv2.Stitcher.create() #create image stitcher


    status, panorama = stitcher.stitch(images) #stitch all image tiles into one overview
    print("number of images: ",len(images))

    if status == cv2.Stitcher_OK:

        output_folder.mkdir(parents=True, exist_ok=True)

        overview_file_name = output_folder / "overview_NEB_function.jpg"  #defines where overview is saved and gives it a name

        if cv2.imwrite(str(overview_file_name), panorama):

            print(f"Stitched image saved to: {overview_file_name.resolve()}")
        else:
            print("ERROR: Could not save the stitched image!")

    #get main project folder
    project_folder = Path(__file__).resolve().parent.parent

    print("=====STITCHING FINISHED=====")

def tile_grid(input_folder,output_folder):

    input_folder = Path(input_folder)
    output_folder = Path(output_folder)

    output_folder.mkdir(parents= True, exist_ok= True)

    tiles = []

    for file in input_folder.glob(".jpg"):

        match = re.search(
            r"ROW(\d+)_COL(\d+)", file.name
    )

    if match:
        row = int(match.group(1))
        col = int(match.group(2))

        image = cv2.imread(str(file))


    max_row = max(row for row, col, image in tiles)
    max_col = max(col for col, row, image in tiles)

    print("=====START TILE GRID=====")





project_folder = Path(__file__).resolve().parent.parent #define project folder location
input_folder = project_folder / "Images" / "Output_Images" / "OutputSlices_003" #folder where the tile set of a scan is located
output_folder = project_folder / "Images" / "Stitched_Images" # folder where the stitch is placed
stitch_images(input_folder, output_folder) #Run stitcher




