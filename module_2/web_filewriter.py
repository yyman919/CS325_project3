"""
web_filewriter.py

This module expects the following input:
- Text content to write to a file
- Output directory for saving the file
- Filename to use for the output file

It writes the provided text content to the specified file within the output directory.

Usage:
python web_filewriter.py <text_content> <output_directory> <output_filename>
"""

import os.path

def write_file(text, output_dir, filename):
    filename = os.path.join(output_dir, filename)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
