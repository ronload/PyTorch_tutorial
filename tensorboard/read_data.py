import os
import numpy as np
from PIL import Image
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")

ANTS_IMAGE_PATH = "data/train/ants_image"
image_folder = sorted(os.listdir(ANTS_IMAGE_PATH))
step = 0

for image_file in image_folder:
    ant_np_image = np.array(Image.open(os.path.join(ANTS_IMAGE_PATH, image_file)))
    if step < 10:
        writer.add_image("First 10 ants", ant_np_image, step, dataformats="HWC")
        step = step + 1

writer.close()