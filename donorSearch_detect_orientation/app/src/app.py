import pandas as pd
import numpy as np
import os
import torch

import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights
from torchvision import transforms
from tqdm.notebook import tqdm
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, classification_report, ConfusionMatrixDisplay, confusion_matrix
from fastai.vision.all import *
import warnings
import logging

warnings.filterwarnings("ignore")

m_logger = logging.getLogger(__name__)
m_logger.setLevel(logging.DEBUG)
handler_m = logging.StreamHandler()
formatter_m = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler_m.setFormatter(formatter_m)
m_logger.addHandler(handler_m)

# Загрузка модели
model = load_learner('my_resnet50_export.pkl')

def predict_orientation(image_path):
    img = PILImage.create(image_path)
    pred, _, _ = model.predict(img)
    return int(pred)


def rotate_and_save(image_path, output_path):
    # Определение ориентации с помощью вашей модели
    orientation = predict_orientation(image_path)

    # Загрузка изображения
    image = Image.open(image_path)

    # Поворот изображения в зависимости от ориентации
    if orientation == 1:
        rotated_image = image.rotate(-90, expand=True)
    elif orientation == 2:
        rotated_image = image.rotate(-180, expand=True)
    elif orientation == 3:
        rotated_image = image.rotate(-270, expand=True)
    else:
        rotated_image = image  # Если ориентация уже 0, оставляем как есть

    # Сохранение повернутого изображения
    rotated_image.save(output_path)
    print(f"Изображение сохранено с ориентацией 0 градусов: {output_path}")
    return f"Изображение сохранено с ориентацией 0 градусов: {output_path}"