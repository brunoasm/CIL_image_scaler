
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# Function definitions (including the provided add_scale_bar function) go here

# Function to read and process the scale_info.csv file
def read_scale_info(csv_path):
    scale_info = pd.DataFrame([{'station': 'green', 'scale_file': 'NikonD5100_10x_P1.tif', 'camera': 'Nikon', 'match_pattern': '10x_P1', 'pixels_per_mm': 3122.0, 'scale_size_mm': 0.1, 'scale_size_pixels': 312.2, 'scale_label': '100 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_10x_P2.tif', 'camera': 'Nikon', 'match_pattern': '10x_P2', 'pixels_per_mm': 3134.0, 'scale_size_mm': 0.1, 'scale_size_pixels': 313.4, 'scale_label': '100 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_10x_P3.tif', 'camera': 'Nikon', 'match_pattern': '10x_P3', 'pixels_per_mm': 3126.0, 'scale_size_mm': 0.1, 'scale_size_pixels': 312.6, 'scale_label': '100 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_5x_P1.tif', 'camera': 'Nikon', 'match_pattern': '5x_P1', 'pixels_per_mm': 1504.0, 'scale_size_mm': 0.5, 'scale_size_pixels': 752.0, 'scale_label': '500 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_5x_P2.tif', 'camera': 'Nikon', 'match_pattern': '5x_P2', 'pixels_per_mm': 1536.0, 'scale_size_mm': 0.5, 'scale_size_pixels': 768.0, 'scale_label': '500 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_5x_P3.tif', 'camera': 'Nikon', 'match_pattern': '5x_P3', 'pixels_per_mm': 1557.0, 'scale_size_mm': 0.5, 'scale_size_pixels': 778.5, 'scale_label': '500 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF2_P1.tif', 'camera': 'Nikon', 'match_pattern': 'CF2_P1', 'pixels_per_mm': 238.8, 'scale_size_mm': 1.0, 'scale_size_pixels': 238.8, 'scale_label': '1 mm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF2_P2.tif', 'camera': 'Nikon', 'match_pattern': 'CF2_P2', 'pixels_per_mm': 336.0, 'scale_size_mm': 1.0, 'scale_size_pixels': 336.0, 'scale_label': '1 mm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF2_P3.tif', 'camera': 'Nikon', 'match_pattern': 'CF2_P3', 'pixels_per_mm': 416.6, 'scale_size_mm': 1.0, 'scale_size_pixels': 416.6, 'scale_label': '1 mm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF3_P1.tif', 'camera': 'Nikon', 'match_pattern': 'CF3_P1', 'pixels_per_mm': 504.0, 'scale_size_mm': 1.0, 'scale_size_pixels': 504.0, 'scale_label': '1 mm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF3_P2.tif', 'camera': 'Nikon', 'match_pattern': 'CF3_P2', 'pixels_per_mm': 862.5, 'scale_size_mm': 0.5, 'scale_size_pixels': 431.25, 'scale_label': '500 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF3_P3.tif', 'camera': 'Nikon', 'match_pattern': 'CF3_P3', 'pixels_per_mm': 703.5, 'scale_size_mm': 0.5, 'scale_size_pixels': 351.75, 'scale_label': '500 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF4_P1.tif', 'camera': 'Nikon', 'match_pattern': 'CF4_P1', 'pixels_per_mm': 784.0, 'scale_size_mm': 1.0, 'scale_size_pixels': 784.0, 'scale_label': '1 mm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF4_P2.tif', 'camera': 'Nikon', 'match_pattern': 'CF4_P2', 'pixels_per_mm': 912.3333333, 'scale_size_mm': 0.5, 'scale_size_pixels': 456.1666667, 'scale_label': '500 µm'},
 {'station': 'green', 'scale_file': 'NikonD5100_CF4_P3.tif', 'camera': 'Nikon', 'match_pattern': 'CF4_P3', 'pixels_per_mm': 1016.0, 'scale_size_mm': 0.5, 'scale_size_pixels': 508.0, 'scale_label': '500 µm'},
 {'station': 'purple', 'scale_file': 'Canon6D_5x_P1.tif', 'camera': 'Canon', 'match_pattern': '5x_P1', 'pixels_per_mm': 1092.5, 'scale_size_mm': 0.5, 'scale_size_pixels': 546.25, 'scale_label': '500 µm'},
 {'station': 'purple', 'scale_file': 'Canon6D_5x_P2.tif', 'camera': 'Canon', 'match_pattern': '5x_P2', 'pixels_per_mm': 1117.0, 'scale_size_mm': 0.5, 'scale_size_pixels': 558.5, 'scale_label': '500 µm'},
 {'station': 'purple', 'scale_file': 'Canon6D_5x_P3.tif', 'camera': 'Canon', 'match_pattern': '5x_P3', 'pixels_per_mm': 1138.666667, 'scale_size_mm': 0.5, 'scale_size_pixels': 569.3333333, 'scale_label': '500 µm'},
 {'station': 'purple', 'scale_file': 'Canon6D_10x_P1.tif', 'camera': 'Canon', 'match_pattern': '10x_P1', 'pixels_per_mm': 2280.0, 'scale_size_mm': 0.1, 'scale_size_pixels': 228.0, 'scale_label': '100 µm'},
 {'station': 'purple', 'scale_file': 'Canon6D_10x_P2.tif', 'camera': 'Canon', 'match_pattern': '10x_P2', 'pixels_per_mm': 2281.0, 'scale_size_mm': 0.1, 'scale_size_pixels': 228.1, 'scale_label': '100 µm'},
 {'station': 'purple', 'scale_file': 'Canon6D_10x_P3.tif', 'camera': 'Canon', 'match_pattern': '10x_P3', 'pixels_per_mm': 2287.0, 'scale_size_mm': 0.1, 'scale_size_pixels': 228.7, 'scale_label': '100 µm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF2_P1.tif', 'camera': 'Canon', 'match_pattern': 'CF2_P1', 'pixels_per_mm': 174.8, 'scale_size_mm': 1.0, 'scale_size_pixels': 174.8, 'scale_label': '1 mm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF2_P2.tif', 'camera': 'Canon', 'match_pattern': 'CF2_P2', 'pixels_per_mm': 237.3, 'scale_size_mm': 1.0, 'scale_size_pixels': 237.3, 'scale_label': '1 mm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF2_P3.tif', 'camera': 'Canon', 'match_pattern': 'CF2_P3', 'pixels_per_mm': 301.4, 'scale_size_mm': 1.0, 'scale_size_pixels': 301.4, 'scale_label': '1 mm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF3_P1.tif', 'camera': 'Canon', 'match_pattern': 'CF3_P1', 'pixels_per_mm': 277.6, 'scale_size_mm': 1.0, 'scale_size_pixels': 277.6, 'scale_label': '1 mm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF3_P2.tif', 'camera': 'Canon', 'match_pattern': 'CF3_P2', 'pixels_per_mm': 296.375, 'scale_size_mm': 1.0, 'scale_size_pixels': 296.375, 'scale_label': '1 mm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF3_P3.tif', 'camera': 'Canon', 'match_pattern': 'CF3_P3', 'pixels_per_mm': 405.6, 'scale_size_mm': 1.0, 'scale_size_pixels': 405.6, 'scale_label': '1 mm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF4_P1.tif', 'camera': 'Canon', 'match_pattern': 'CF4_P1', 'pixels_per_mm': 575.0, 'scale_size_mm': 1.0, 'scale_size_pixels': 575.0, 'scale_label': '1 mm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF4_P2.tif', 'camera': 'Canon', 'match_pattern': 'CF4_P2', 'pixels_per_mm': 654.0, 'scale_size_mm': 1.0, 'scale_size_pixels': 654.0, 'scale_label': '1 mm'},
 {'station': 'purple', 'scale_file': 'Canon6D_CF4_P3.tif', 'camera': 'Canon', 'match_pattern': 'CF4_P3', 'pixels_per_mm': 740.3333333, 'scale_size_mm': 1.0, 'scale_size_pixels': 740.3333333, 'scale_label': '1 mm'}])
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

# GUI Application
class ScaleBarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Scale Bar Application')
        self.geometry('400x300')

        self.create_widgets()
        self.csv_path = 'scale_info.csv'  # Update with the actual path of the CSV file
        self.scale_info = read_scale_info(self.csv_path)
        self.output_dir = "images_with_scale"
        self.selected_files = []

    def create_widgets(self):
        # Button to select files
        self.select_button = tk.Button(self, text='Select Images', command=self.select_files)
        self.select_button.pack(pady=10)

        # Listbox to display selected files
        self.file_listbox = tk.Listbox(self)
        self.file_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Button to process files
        self.process_button = tk.Button(self, text='Process Images', command=self.process_files)
        self.process_button.pack(pady=10)

    def select_files(self):
        filetypes = [('Image files', '*.tif *.tiff')]
        filenames = filedialog.askopenfilenames(title='Select Images', filetypes=filetypes)
        self.selected_files = filenames
        self.update_file_listbox()

    def update_file_listbox(self):
        self.file_listbox.delete(0, tk.END)
        for file in self.selected_files:
            self.file_listbox.insert(tk.END, file)

    def process_files(self):
        for file in self.selected_files:
            add_scale_bar(file, self.scale_info, 100, 100, self.output_dir)
        messagebox.showinfo('Process Complete', 'All selected images have been processed.')

if __name__ == "__main__":
    app = ScaleBarApp()
    app.mainloop()
