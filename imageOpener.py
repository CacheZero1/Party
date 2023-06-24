# Imports (modules)
from PIL import Image


# Image opener
def getImg(url: str):
    """Get the Image

    Args:
        url (str): Image url

    Returns:
        Image: return the Image
    """
    originalImg = Image.open(url)
    return originalImg


# get Previews
def getPreviews():
    """Return all the previews

    Returns:
        Image: return the Image
    """
    # Preview Images
    beachIslandsPreview = getImg("./beachIslands/beachIslandsPreview.png")
    
    return beachIslandsPreview