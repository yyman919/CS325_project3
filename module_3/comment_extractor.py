"""
comment_extractor.py

This module expects the following input:
- Path to an HTML file (input_file) from which comments will be extracted

It extracts comments from the specified HTML file and saves them to separate text files in the 'Data/processed' directory. The extracted comments are saved as 'comments1.txt', 'comments2.txt', and so on.

Usage:
python comment_extractor.py <input_file>
"""

import sys
from bs4 import BeautifulSoup
import os

# Function to extract comments from an HTML file
def extract_comments(input_file, output_dir):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            text = infile.read()

        soup = BeautifulSoup(text, 'html.parser')

        def is_valid_paragraph(tag):
            return tag.name == 'p' and not tag .has_attr('class')

        paragraphs = soup.find_all(is_valid_paragraph)
        comments = []

        for paragraph in paragraphs:
            comment_text = paragraph.get_text().strip()

            if comment_text:
                comments.append(comment_text)

        if not comments:
            print("No comments found in the input file.")
        else:
            output_dir = 'Data/processed'
            count = 1
            while True:
                output_file = os.path.join(output_dir, f'comments{count}.txt')
                if not os.path.exists(output_file):
                    break
                count += 1

            with open(output_file, 'w', encoding='utf-8') as outfile:
                for comment in comments:
                    outfile.write(comment + '\n\n')

            print(f"Comments extracted and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 comment_extractor.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = 'Data/processed'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    extract_comments(input_file, output_dir)
