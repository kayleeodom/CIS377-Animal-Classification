# This allows us to "download the dataset without having to download it on our computer". However you do have to use your kaggle api

import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset identifier (can be found on the Kaggle dataset page URL)
dataset = 'alessiocorrado99/animals10'

# Download the dataset
output_path ='csv/'  # Local folder to save the dataset
os.makedirs(output_path, exist_ok=True)

# Download and unzip the dataset
api.dataset_download_files(dataset, path=output_path, unzip=True)

print(f"Dataset downloaded and saved to {output_path}")
