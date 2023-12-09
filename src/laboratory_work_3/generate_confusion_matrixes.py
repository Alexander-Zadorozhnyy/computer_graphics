import os
import shutil
import glob
from pathlib import Path

import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
from ultralytics import YOLO


def load_data(folder):
    images = []
    labels = []
    extensions = ["jpeg", "jpg", "png"]
    folder_path = Path(os.path.join(os.getcwd(), folder))
    label = folder.split("/")[-1]

    all_files = [x for x in os.listdir(folder_path) if x.split(".")[-1] in extensions]

    for filename in all_files[:100]:
        # Load image
        # image = cv2.imread(filename)
        images.append(os.path.join(folder_path, filename))
        # Extract label from filename (modify based on your naming convention)
        labels.append(label)  # Replace "class_name" with your actual label
    return images, labels


def generate_confusion_matrix(model, images, labels):
    # Predict on each image
    predictions = []
    names = model.names
    for image in images:
        # Use YOLOv8 to predict on the image
        prediction = model(image)[0]
        # Extract predicted class
        prediction_class = names[int(torch.topk(prediction.probs, k=1).indices[0])]
        predictions.append(prediction_class)

    # Generate confusion matrix
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

    cm = confusion_matrix(labels, predictions, labels=np.unique(labels))

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(labels))
    disp.plot()
    plt.savefig(
        os.path.join("media", "matrixes", "_".join(list(np.unique(labels))) + "_cm.png")
    )
    return cm


# Load the YOLOv8 model
model = YOLO("./models/animals_classifier.pt")
classes = list(model.names.values())
classes.remove("red_panda")

# Load images and labels for panda folder
panda = "./datasets/dataset/test/red_panda"
images_panda, labels_panda = load_data(panda)
for _class in classes:
    another = f"./datasets/dataset/test/{_class}"
    images, labels = load_data(another)
    # Generate and save confusion matrices
    generate_confusion_matrix(model, images_panda + images, labels_panda + labels)
