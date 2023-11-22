import numpy as np
from PIL import Image
from torch.utils.tensorboard import SummaryWriter

# define writer
writer = SummaryWriter(log_dir="logs")

# define path
ant_image_path = "data/train/ants_image/0013035.jpg"
bee_image_path = "data/train/bees_image/16838648_415acd9e3f.jpg"

# transform PIL image into np.array
ant_nparray = np.array(Image.open(ant_image_path))
bee_nparray = np.array(Image.open(bee_image_path))

# show tensorboard
tag = "read_data"
writer.add_image(tag, ant_nparray, 1, dataformats="HWC")
writer.add_image(tag, bee_nparray, 2, dataformats="HWC")

# close writer
writer.close()


