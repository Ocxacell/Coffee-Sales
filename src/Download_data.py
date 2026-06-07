from dotenv import load_dotenv
import kagglehub
import os

load_dotenv()


path = kagglehub.dataset_download("hosubjeong/bakery-sales",output_dir="./data")

print("Path to dataset files:", path)