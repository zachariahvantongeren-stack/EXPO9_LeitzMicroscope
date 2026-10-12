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

def tile_grid(input_folder,output_folder, overlap = 0.3):

    print("=====START TILE GRID STITCHER=====")

    input_folder = Path(input_folder)
    output_folder = Path(output_folder)

    output_folder.mkdir(parents= True, exist_ok= True)

    tiles = []

    for file in input_folder.glob("*.jpg"):
        match = re.search(r"tile_ROW(\d+)_COL(\d+)", file.name)

        if match:
            row = int(match.group(1))
            col = int(match.group(2))

            image = cv2.imread(str(file))

            if image is not None:
                tiles.append((row, col, image))

    if not tiles:
        print("No valid tiles found. Check the folder and filenames.")
        return
        

    if match:
        row = int(match.group(1))
        col = int(match.group(2))

        image = cv2.imread(str(file))

        if image is None:
            tiles.append((row,col,image))

    tile_height, tile_width = tiles[0][2].shape[:2]
    step_x = int(tile_width * (1- overlap))
    step_y = int(tile_height * (1- overlap))


    rows = max(tile[0] for tile in tiles) + 1
    cols = max(tile[1] for tile in tiles) + 1

    canvas = tiles[0][2].copy()

    canvas = cv2.copyMakeBorder(
        canvas,
        0, rows * step_x,
        0, cols * step_y,
        cv2.BORDER_CONSTANT,
        value=(0, 0, 0)
     )

    for row, col, image in tiles:
        x = col * step_x
        y = row * step_y
        height, width = image.shape[:2]

        canvas[y:y+height, x:x+width] = image

    output_folder.mkdir(parents=True, exist_ok=True)
    output_file = output_folder / "overview_grid_2.jpg"

    cv2.imwrite(str(output_file), canvas)
    print("Saved grid to:", output_file.resolve())


project_folder = Path(__file__).resolve().parent.parent #define project folder location
input_folder = project_folder / "Images" / "Output_Images" / "OutputSlices_002" #folder where the tile set of a scan is located
output_folder = project_folder / "Images" / "Stitched_Images" # folder where the stitch is placed
#stitch_images(input_folder, output_folder) #Run stitcher
tile_grid(input_folder, output_folder)




