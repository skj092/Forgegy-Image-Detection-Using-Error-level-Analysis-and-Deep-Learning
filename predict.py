# This script will predict the class of an image using a trained deep learning model.
import argparse
import json
import numpy as np
import os
import torch, torchvision
from torch import nn
from PIL import Image, ImageChops, ImageEnhance
from glob import glob
from torchvision import transforms
from models import CNN


# preprocess image
def convert_to_ela_image(image_path, quality=90):
    """Converts an image to an ELA image.
    :param image_path: Path to the image
    :param quality: Quality of the image to be saved
    :return: ELA image
    """
    # Save the image at the given quality
    temp_file = 'temp.jpg'
    im = Image.open(image_path)
    im.save(temp_file, 'JPEG', quality=quality)

    # Open the saved image and the original image
    saved = Image.open(temp_file)
    orignal = Image.open(image_path)

    # Find the absolute difference between the images
    diff = ImageChops.difference(orignal, saved)

    # Normalize the difference by multiplying with a scale factor and convert to grayscale
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    scale = 255.0 / max_diff
    diff = ImageEnhance.Brightness(diff).enhance(scale)

    # Remove the temporary file
    os.remove(temp_file)

    return diff

# model
def load_model(model_path):
    # for cnn model
    if model_path == 'cnn.pth':
        model = CNN()
        model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        return model
    # for resnet model
    else:
        model = torch.load(model_path, map_location=torch.device('cpu'))
        return model
    
# predict
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_image(image_path, model):
    img = convert_to_ela_image(image_path)
    img = transform(img)
    img = img.unsqueeze(0)
    model.eval()
    with torch.no_grad():
        output = model(img)
        _, pred = torch.max(output, 1)
    return 'fake' if pred.item() == 1 else 'real'

# main
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str, help='Path to image')
    parser.add_argument('--model_path', type=str, help='Path to model')
    args = parser.parse_args()
    model = load_model(args.model_path)
    prediction = predict_image(args.image_path, model)
    print(prediction)

if __name__ == '__main__':
    main()