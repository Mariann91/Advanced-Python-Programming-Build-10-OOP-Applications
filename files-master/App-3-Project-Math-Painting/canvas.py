import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        # creates an array that shapes the object: height, width, depth
        self.data = np.zeros((self.height, self.width, 3), dtype="uint8")
        # adjusting color in RGB format
        self.data[:] = self.color

    def make(self, image_path):
        # creates image from an array
        img = Image.fromarray(self.data, "RGB")

        # saves image
        img.save(image_path)
