import os
import requests
import pandas as pd

def download_images(image_links, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)  # Create the folder if it doesn't exist

    for idx, link in enumerate(image_links):
        try:
            response = requests.get(link)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Generate an appropriate file name, e.g., image_0.jpg, image_1.jpg, etc.
            file_name = f"image_{idx}.jpg"
            file_path = os.path.join(download_folder, file_name)
            
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {file_name}")
        except Exception as e:
            print(f"Failed to download {link}: {e}")

# Example usage
if _name_ == "_main_":
    # Assuming you have a DataFrame with your dataset
    # For demonstration, I'll create a sample DataFrame
    
    # Call the function with the image links and your desired download folder
    download_images(df['image_link'], 'Images/')