# Week 6 – File I/O (CS50P)

## Overview

In Week 6, I learned how to work with files in Python, including reading and writing text files, CSV files, and images. I also learned how to use command-line arguments to specify input and output files.

## Topics Covered

- Reading and writing files
- Command-line arguments (`sys.argv`)
- Exception handling (`FileNotFoundError`)
- CSV files with `csv.DictReader` and `csv.DictWriter`
- Image processing using the Pillow (`PIL`) library

## Problems Completed

### 1. lines.py
Counts the number of lines of code in a Python source file while ignoring blank lines and comments.

### 2. pizza.py
Reads a CSV file containing pizza menu data and displays it in a formatted table.

### 3. scourgify.py
Reads a CSV file with names stored as `"last, first"` and creates a new CSV file with separate `first`, `last`, and `house` columns.

### 4. shirt.py
Resizes and crops an image to match the dimensions of `shirt.png`, overlays the shirt image onto it, and saves the final result.

## Skills Learned

- Using `sys.argv`
- Working with files using `open()`
- Reading CSV files with `DictReader`
- Writing CSV files with `DictWriter`
- Splitting and cleaning strings using `split()` and `strip()`
- Opening, resizing, editing, and saving images with Pillow
- Handling file-related errors using `try` and `except`

## Technologies Used

- Python 3
- csv module
- Pillow (PIL)
- os module
- sys module
