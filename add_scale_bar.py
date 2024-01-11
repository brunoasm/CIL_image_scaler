
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# Function to read and process the scale_info.csv file
def read_scale_info(csv_path):
    scale_info = pd.read_csv(csv_path)
    return scale_info

# Function to add a scale bar to an image
def add_scale_bar(image_path, scale_info, x_coord, y_coord, output_dir):
    original_file_name=os.path.basename(image_path)

    # Determine the scale size and label based on camera make and match pattern
    scale_row = scale_info[scale_info['match_pattern'].apply(lambda x: x in original_file_name)]
    if scale_row.empty:
        print("No matching scale information found.")
        return None

    scale_size_pixels = int(scale_row.iloc[0]['scale_size_pixels'])
    scale_label = scale_row.iloc[0]['scale_label']

    # Read the original image
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)
        
        # Adjust y_coord for bottom-left origin
        width, height = img.size
        y_coord = height - y_coord
        
        # Draw the scale bar
        draw.rectangle([(x_coord, y_coord), (x_coord + scale_size_pixels, y_coord+10)], fill="white")
        
        # Add scale label
        try:
            font = ImageFont.truetype("Arial Bold.ttf", 60)  # Using Arial font
        except IOError:
            font = ImageFont.load_default()
        draw.text((x_coord, y_coord - 65), scale_label, fill="white", font=font)
        
        # Save the image
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(image_path))[0] + "_scaled.tif")
        img.save(output_file_path)

    return output_file_path

# Sample usage
csv_path = 'scale_info.csv'  # Update with the actual path of the CSV file
scale_info = read_scale_info(csv_path)
image_path = '4429479_Oxycorynus_melanocerus_h_d_CF3_P1_HF23.tif'
output_dir = "images_with_scale"

add_scale_bar(image_path, scale_info,  100, 100, output_dir) 
