import os
import re
import pytesseract
from PIL import Image
from tkinter import filedialog
from tkinter import Tk

# Set the path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the regular expression pattern for the desired naming structure
pattern = r'[a-zA-Z0-9]{5}-\d+'

# Prompt user to select an image file
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[('Image files', '*.jpg *.jpeg *.png')])

# Open the image using PIL
img = Image.open(file_path)

# Use Tesseract to extract text from the image
text = pytesseract.image_to_string(img)

# Search for a match to the naming structure in the extracted text
match = re.search(pattern, text)

# If a match is found, extract the new file name
if match:
    # Construct the new file name
    new_name = f'{match.group()}.jpg'
    # Rename the image file
    os.rename(file_path, new_name)
    print(f'Image renamed from {file_path} to {new_name}.')
else:
    print(f'No match found in {file_path}.')
    print(text)
