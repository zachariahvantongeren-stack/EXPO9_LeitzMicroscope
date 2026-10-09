import cv2
from pathlib import Path

print("=====STARTING STITCHING=====")

#get main project folder
project_folder = Path(__file__).resolve().parent.parent

image_folder = project_folder / "Images" / "Output_Images" / "OutputSlices_008" #folder where the tile set of a scan is located

files = list(image_folder.glob("*.jpg")) #find all jpg files belonging to the scan

images = []

#for loop to read all the files
for filename in files:

    image = cv2.imread(str(filename))

    if image is not None:
        images.append(image)

print("number of images: ",len(images))


stitcher = cv2.Stitcher.create() #create image stitcher

status, panorama = stitcher.stitch(images) #stitch all image tiles into one overview

if status == cv2.Stitcher_OK:

    overview_file_name = f"Images/Stitched_Images/overview_SiliconWafer200.jpg" #defines where overview is saved and gives it a name

    cv2.imwrite(overview_file_name , panorama) #writes to folder
    print("stitched image")
else:
    print("stitching failed:", status)

print("=====STITCHING FINISHED=====")

