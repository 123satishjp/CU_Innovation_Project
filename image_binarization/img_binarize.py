from PIL import Image
from skimage.filters import threshold_otsu
import numpy as np
import time
# Open the image and convert to grayscale
img = Image.open(r"/home/scrad/Pictures/saif.jpg").convert('L')

# Convert the image to a numpy array
img = np.array(img)

# Threshold the image
threshold_value = threshold_otsu(img)
thresholded_img = Image.fromarray((img > threshold_value).astype(np.uint8) * 255)

# Save the thresholded image
thresholded_img.save('thresholded_image.jpg')
