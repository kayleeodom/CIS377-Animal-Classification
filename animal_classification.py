import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset identifier (can be found on the Kaggle dataset page URL)
dataset = 'dataset-owner/dataset-name'

# Download the dataset
output_path = 'datasets/'  # Local folder to save the dataset
os.makedirs(output_path, exist_ok=True)

# Download and unzip the dataset
api.dataset_download_files(dataset, path=output_path, unzip=True)

print(f"Dataset downloaded and saved to {output_path}")
