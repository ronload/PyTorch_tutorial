# This file is used to create the labels folder by images folder

import os

root_dir = "test_dataset/train"
target_dir = "bees_image"
image_list = os.listdir(os.path.join(root_dir, target_dir))
label = ("bees")
out_dir = "bees_label"
for i in image_list:
    file_name = i.split(".jpg")[0]
    with open(os.path.join(root_dir, out_dir, "{}.txt".format(file_name)), 'w') as f:
        f.write(label)