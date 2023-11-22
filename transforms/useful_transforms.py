# This file is used to perform some useful transforms
from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

# define writer
writer = SummaryWriter("logs")

# open image
image_path = "test_dataset/train/ants_image/0013035.jpg"
image_PIL = Image.open(image_path)

# ``transforms.ToTensor()``
trans_ToTensor = transforms.ToTensor()  # define a transformer
image_tensor = trans_ToTensor(image_PIL)
writer.add_image("image(PIL) -> image(tensor)", image_tensor, 1)

# ``transforms.Normalize()``
print(image_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])  # define a normalizer
image_norm = trans_norm(image_tensor)
print(image_norm[0][0][0])
writer.add_image("image -> image(normalize)", image_norm, 1)

# ``transforms.Resize()``
print("Before resize: " + str(image_PIL.size))
trans_resize = transforms.Resize((512, 512))
image_PIL_resize = trans_resize(image_PIL)
print("After resize: " + str(image_PIL_resize.size))
writer.add_image("image -> image(resize)", trans_ToTensor(image_PIL_resize), 1)

# ``transforms.Compose()``
tran_compose = transforms.Compose([
    trans_resize,
    trans_ToTensor
])
image_compose = tran_compose(image_PIL)
writer.add_image("image -> image(compose: resize, tensor)", image_compose, 1)

# ``transforms.RandomCrop()``
trans_random_crop = transforms.RandomCrop((50, 100))
trans_compose_2 = transforms.Compose([
    trans_random_crop,
    trans_ToTensor
])
for i in range(10):
    writer.add_image(
        tag="image -> image(compose: random_crop, tensor)",
        img_tensor=trans_compose_2(image_PIL),
        global_step=i
    )  # random crop the original PIL image to 10 (50*100) tensor images

# close writer
writer.close()