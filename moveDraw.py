
from PIL import Image


def getImg():
    originalImg = Image.open("./beachIslands/beachIslandsMap.png")
    width, height = originalImg.size

    for x in range(width):
        for y in range(height):
            if x == 19 and y == 32:
                originalImg.putpixel((x, y), (0, 0, 0, 255))
            else:
                pass
            
    return originalImg
    