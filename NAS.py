import os
import time
import shutil

# Configuration
download_folder = "C:/Users/YourUsername/Downloads"
nas_folder = "//NAS_Server/Shared_Folder"  # Replace with your NAS server's shared folder path

def upload_to_nas(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Uploaded {filename} to NAS server")

while True:
    upload_to_nas(download_folder, nas_folder)
    time.sleep(1800)  # Sleep for 30 minutes (30 minutes * 60 seconds)

