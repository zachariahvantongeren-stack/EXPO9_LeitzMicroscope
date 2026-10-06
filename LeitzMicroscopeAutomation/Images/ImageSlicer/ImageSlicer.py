import cv2



IP_IMAGE = cv2.imread("Images/ImageSlicer/InputImages/IP_CrabNebula.jpg")

IMAGE_WIDTH, IMAGE_HEIGHT, channel = IP_IMAGE.shape

print(IP_IMAGE.shape)


TILE_SIZE = 500

tile_number = 1

for y in range(0, IMAGE_HEIGHT ,TILE_SIZE):
    for x in range(0, IMAGE_WIDTH, TILE_SIZE):

        tile = IP_IMAGE[y:y+TILE_SIZE, x:x+TILE_SIZE]

        filename = f"Images/ImageSlicer/OutputImages/tile_{tile_number : 03d}.jpg"

        cv2.imwrite(filename, tile)

        tile_number += 1



