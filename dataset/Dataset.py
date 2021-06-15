import os
import cv2
import torch
from torch.utils.data import Dataset

class BettaDataset(Dataset):
    def __init__(self):
        self.images_dir = "betta_60"
        image_list = os.listdir(self.images_dir)
        print("Dataset contains ", len(image_list), " betta images.")
        self.data = []
        for image_name in image_list:
            image_label = "betta"
            image_path = self.images_dir + os.sep + image_name
            self.data.append([image_path, image_label])
        self.class_map = {"betta" : 0}
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idex):
        image_path, class_name = self.data[idex]
        image = cv2.imread(image_path)
        class_id = self.class_map[class_name]
        image_tensor = torch.from_numpy(image) / 255
        image_tensor = image_tensor.permute(2, 0, 1)
        return image_tensor, class_id