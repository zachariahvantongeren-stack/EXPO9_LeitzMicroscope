import cv2
import glob


images = []


for filename in glob.glob("testImages/*.jpeg"):

    image = cv2.imread(filename)

    if image is not None:
        images.append(image)

print("images",len(image))


stitcher = cv2.Stitcher.create()


status, panorama = stitcher.stitch(image)

if status == cv2.Stitcher_OK:

    cv2.imwrite("overview.jpeg", panorama)
    print("stitched")
else:
    print("not stitched:", status)


