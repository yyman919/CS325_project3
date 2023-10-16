"""
web_downloader.py

This module expects the following input:
- URL of the content to download (e.g., 'http://example.com')
- Output directory for saving the downloaded content (e.g., 'Data/raw')

It downloads content from the specified URL and saves it to a text file in the output directory. The output filename is determined automatically with an incrementing number, such as 'file1.txt', 'file2.txt', and so on.

Usage:
python web_downloader.py <URL> <output_directory>
"""

import urllib.request
import sys
import argparse
import os

# Function to download the content of the URL
def download(url, output_dir):
    try:
        # Open the URL and read its content
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        
        # Determine the next available output file name (file1.txt, file2.txt, etc.)
        count = 1
        while True:
            filename = f'file{count}.txt'
            output_file = os.path.join(output_dir, filename)
            if not os.path.exists(output_file):
                break
            count += 1
        
        # Write the downloaded content to the determined filename
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f"Content downloaded and saved to {output_file}")
    except urllib.error.URLError as e:
        print(f"Error: Unable to access the URL - {e.reason}")
        sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        sys.exit(1)

# Main function for downloading
def main():
    parser = argparse.ArgumentParser(description='Download content from a URL and save it to a text file.')
    parser.add_argument('url', type=str, help='URL to download content from (include http:// or https://)')
    parser.add_argument('output_dir', type=str, help='Output directory for saving the file')

    args = parser.parse_args()
    url = args.url
    output_dir = args.output_dir

    if not url.startswith('http://') and not url.startswith('https://'):
        print('Error: Invalid URL. Please include http:// or https://')
        sys.exit(1)

    download(url, output_dir)

if __name__ == '__main__':
    main()
