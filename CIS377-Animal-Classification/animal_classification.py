# data_utils.py

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore

# Translation dictionary for class labels
TRANSLATE = {
    "cane": "dog", "cavallo": "horse", "elefante": "elephant",
    "farfalla": "butterfly", "gallina": "chicken", "gatto": "cat",
    "mucca": "cow", "pecora": "sheep", "scoiattolo": "squirrel",
    "dog": "cane", "cavallo": "horse", "elephant": "elefante",
    "butterfly": "farfalla", "chicken": "gallina", "cat": "gatto",
    "cow": "mucca", "spider": "ragno", "squirrel": "scoiattolo"
}

def get_data_generators(directory, target_size=(224, 224), batch_size=32, validation_split=0.15):
    """Create training and validation data generators with augmentation."""
    datagen = ImageDataGenerator(
        rescale=1/255.,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=validation_split
    )
    
    train_generator = datagen.flow_from_directory(
        directory,
        target_size=target_size,
        batch_size=batch_size,
        shuffle=True,
        subset='training',
        class_mode='categorical'
    )
    
    validation_generator = datagen.flow_from_directory(
        directory,
        target_size=target_size,
        batch_size=batch_size,
        shuffle=False,
        subset='validation',
        class_mode='categorical'
    )
    
    return train_generator, validation_generator

def translate_labels(class_labels):
    """Translate class labels using the predefined dictionary."""
    return [TRANSLATE.get(label, label) for label in class_labels]

def display_translated_labels(train_generator):
    """Translate and display class labels."""
    class_labels = list(train_generator.class_indices.keys())
    translated_labels = translate_labels(class_labels)
    print(f"Original Class Labels: {class_labels}")
    print(f"Translated Class Labels: {translated_labels}")
    return class_labels, translated_labels
