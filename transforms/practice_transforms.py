# This file is used to practice ``torchvision.transforms``

import cv2
from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

"""
Explain what is ``tensor``
Use ``transforms.ToTensor()`` to analyse two problem
    1. How to use ``transforms`` in python?
    2. What is the difference between ``tensor`` and other data types?
"""

# Use ants[0] to perform
image_path = "test_dataset/train/ants_image/0013035.jpg"
image_PIL = Image.open(image_path)  # type(image_PIL) -> PIL.JpegImagePlugin.JpegImageFile
image_cv = cv2.imread(image_path)  # type(image_cv) -> numpy.ndarray

writer = SummaryWriter("logs")  # create a tensorboard

# Declare a ``transforms.ToTensor``
tensor_transformer = transforms.ToTensor()

# Transform a ``PIL image`` or ``numpy.ndarray`` to a ``tensor``
image_tensor = tensor_transformer(image_PIL)  # type(image_tensor) -> torch.Tensor
# image_tensor = tensor_transformer(image_cv)  # type(image_cv) -> torch.Tensor

writer.add_image("Tensor image", image_tensor, 1)

writer.close()