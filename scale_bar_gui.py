
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os, sys

# Function definitions (including the provided add_scale_bar function) go here

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

csv_path = resource_path('scale_info.csv')


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
