"""
run.py

This script expects the following input:
- URL of the content to download and extract comments from

It runs the web_downloader.py module to download content from the specified URL and save it to a text file in the 'Data/raw' directory. It then runs the comment_extractor.py module to extract comments from the downloaded content and save them to separate text files in the 'Data/processed' directory.

Usage:
python run.py <URL>
"""

import sys
import os
import subprocess

# Function to run web_downloader.py
def run_web_downloader(url, output_dir):
    try:
        subprocess.run(['python', 'module_1/web_downloader.py', url, output_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running web_downloader.py: {e}")

# Function to run comment_extractor.py
def run_comment_extractor(input_file, output_dir):
    try:
        subprocess.run(['python', 'module_3/comment_extractor.py', input_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running comment_extractor.py: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 run.py URL")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = 'Data/raw'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Run the web downloader to download content from the URL and save it to a text file
    print(f"Downloading content from URL: {url}")
    run_web_downloader(url, output_dir)

    # Determine the generated filename by web_downloader.py (the latest file)
    filenames = os.listdir(output_dir)
    if filenames:
        latest_filename = max(filenames, key=lambda x: int(x.lstrip("file").rstrip(".txt")))
        print(f"Using file for comment extraction: {latest_filename}")
        run_comment_extractor(os.path.join(output_dir, latest_filename), 'Data/processed')
    else:
        print("No files found for comment extraction.")

if __name__ == '__main__':
    main()
