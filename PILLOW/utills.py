from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

def out_file(filename):
    return os.path.join(OUTPUT_FOLDER, filename)