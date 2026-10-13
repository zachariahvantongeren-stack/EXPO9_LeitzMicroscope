import cv2
from pathlib import Path


print("=====STARTING IMAGE SLICER=====")

def slicer_load_images(image_path):

    image = cv2.imread(str(image_path))

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")
       
    return image
     
def slice_Image(image, scan_folder, TILE_SIZE = 100 ,TILE_OVERLAP = 0.2):

    #gets the image height, width, and color channels. slicer needs it to determine how much to move.
    IMAGE_HEIGHT, IMAGE_WIDTH = image.shape[:2]
    print(image.shape)
    
    #calculate how far slicer needs to move for each tile.
    TILE_STEP = int(TILE_SIZE*(1 - TILE_OVERLAP))

    if TILE_SIZE <= 0 or not 0 <= TILE_OVERLAP < 1:
        raise ValueError("ERROR: 0 <= TILESIZE and 0 < TILE_OVERLAP < 0 ")

    #start with tile = 0
    tile_number = 0

    #for loop to create a set of tiles
    for ROW, y in enumerate(range(0, IMAGE_HEIGHT ,TILE_STEP)): #for the tiles in the y-axis, take predefined steps from 0 until IMAGE_HEIGHT with steps of size TILE_STEP
        for COL, x in enumerate(range(0, IMAGE_WIDTH, TILE_STEP)): #for the tiles in x-axis, take predefined steps from 0 until IMAGE_WIDTH with steps of size TILE_STEP

            tile = image[y:y+TILE_SIZE, x:x+TILE_SIZE] # get section of the original input using the X and Y values

            filename = scan_folder / f"tile_ROW{ROW:03d}_COL{COL:03d}.jpg" #file gets a name and goes to scan_folder  

            cv2.imwrite(str(filename), tile) #writing image tile to the folder

            tile_number += 1 #iterate by +1

    #print final tile count
    print(f"image sliced into {tile_number} tiles")
    print("=====SLICER FINISHED=====")


# get the main project folder based on where the file is and defines where the generated images should be stored
project_folder = Path(__file__).resolve().parent.parent
output_folder = project_folder / "Images" / "Output_Images"

#checks if output folder exists, if not, create one
output_folder.mkdir(parents=True, exist_ok= True)

scan_number = 1

#while loop to create a new folder for each scan, if folder exists increase the scan_number by +1
while True:
    scan_folder = output_folder / f"OutputSlices_{scan_number:03d}"

    if not scan_folder.exists():

        scan_folder.mkdir()

        break

    scan_number += 1

print("output tiles in: ", scan_folder)

#OpenCV reads the image inside the input folder
input_file = project_folder / "Images" / "Input_Images" / "IP_SiliconWafer.jpg"
print(f"image name: {input_file.name}")

INPUT_IMAGE = slicer_load_images(input_file)
slice_Image(INPUT_IMAGE,scan_folder)
