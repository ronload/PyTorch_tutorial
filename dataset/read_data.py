# This file is used to make a self define dataset
import os
from PIL import Image
from torch.utils.data import Dataset

ROOT_PATH = "test_dataset/train"

class Sample:
    def __init__(self, name, image, label):
        """
        Represent a sample in the dataset.
        :param name:
        :param image:
        :param label:
        """
        self.name = name
        self.image = image
        self.label = label
    def __str__(self):
        return f"Sample(name: {self.name}, image: {self.image}, label: {self.label})"

class MyDataset(Dataset):
    def __init__(self, label):
        self.names = self.__get_names__(label)
        self.images = self.__get_images__(label)
        self.labels = self.__get_labels__(label)
    def __getitem__(self, index):
        return Sample(
            name=self.names[index],
            image=self.images[index],
            label=self.labels[index]
        )
    def __len__(self):
        return len(self.names)
    @staticmethod
    def __get_names__(label):
        folder = os.listdir(os.path.join(ROOT_PATH, label + "_image"))
        names = []
        for file_name in folder:
            names.append(file_name.split(".jpg")[0])
        return names
    @staticmethod
    def __get_images__(label):
        path = os.path.join(ROOT_PATH, label + "_image")
        image_folder = os.listdir(path)
        images = []
        for image_file in image_folder:
            images.append(Image.open(os.path.join(path, image_file)))
        return images
    @staticmethod
    def __get_labels__(label):
        path = os.path.join(ROOT_PATH, label + "_label")
        label_folder = os.listdir(path)
        labels = []
        for label_file in label_folder:
            label_file_path = os.path.join(path, label_file)
            with open(label_file_path, 'r') as label_file_content:
                labels.append(label_file_content.readline())
        return labels

ants = MyDataset("ants")
bees = MyDataset("bees")

for ant in ants:
    print(ant)

for bee in bees:
    print(bee)
