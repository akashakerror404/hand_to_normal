Handwritten Text to Normal Text Converter

This project uses PaddleOCR to convert handwritten text into digital text.

Features

Extract text from handwritten images

Supports multiple languages

Lightweight and fast processing

Setup (Beginner Friendly Guide)

Step 1: Install Python

Make sure you have Python installed on your system. You can download it from python.org.

Check if Python is installed by running:

Step 2: Create a Virtual Environment

A virtual environment helps manage dependencies for your project.

Run the following commands:

For macOS/Linux:

For Windows:

Step 3: Install Dependencies

Make sure you have a requirements.txt file with all necessary packages listed. Then run:

Step 4: Set Up Django

If you don’t have Django installed, install it using:

Step 5: Run Migrations (If needed)

Step 6: Run the Django Project

Start the Django server using:

Now, open your browser and visit http://127.0.0.1:8000/ to see your project running.

Usage (Handwritten Text Conversion)

Step 1: Import Necessary Libraries

Step 2: Initialize the OCR Engine

Step 3: Process an Image

Replace 'handwritten_image.jpg' with the path to your image.

Example Output

Notes

Ensure the image has clear handwriting for best results.

Adjust PaddleOCR parameters for better accuracy.

License

This project is open-source and available under the MIT License.
