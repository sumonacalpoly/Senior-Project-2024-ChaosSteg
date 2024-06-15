import os
import numpy as np
from PIL import Image
import random
import shutil
import random

#UNECESSEARY NOW
def split_dataset(image_folder, train_folder, test_folder, train_size=381, test_size=163):
    if not os.path.exists(train_folder):
        os.makedirs(train_folder)
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    
    all_images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    random.shuffle(all_images)
    
    train_images = all_images[:train_size]
    test_images = all_images[train_size:train_size+test_size]
    
    for img in train_images:
        shutil.move(os.path.join(image_folder, img), os.path.join(train_folder, img))
    for img in test_images:
        shutil.move(os.path.join(image_folder, img), os.path.join(test_folder, img))
    
    print(f"Moved {len(train_images)} images to {train_folder}")
    print(f"Moved {len(test_images)} images to {test_folder}")

image_folder = r""
train_folder = r""
test_folder = r""

split_dataset(image_folder, train_folder, test_folder)