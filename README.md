# Text Processing Script

This Python script processes a text input, counts the number of words, and converts the text to uppercase. The results are saved to an output file.

## Features

- Reads predefined text from `input.txt`.
- Counts the total number of words.
- Converts the text to uppercase.
- Writes the results, including the word count, to `output.txt`.
- Prompts the user for a filename and handles errors if the file doesn’t exist or can’t be read.

## How It Works

1. **Define Input Text**: The script starts with a predefined list of strings representing the input text.
2. **Write to `input.txt`**: It writes the input text to a file named `input.txt`.
3. **Read and Process**:
   - Reads content from `input.txt`.
   - Splits the content into words and counts them.
   - Converts the content to uppercase.
4. **Write Results to `output.txt`**: The script creates or overwrites `output.txt` with the word count and the uppercase text.
5. **Display Output**: Finally, it reads and displays the contents of `output.txt`.
6. **Error Handling Lab**: The script allows the user to input a filename and handles errors if the specified file does not exist or cannot be read.

## Usage

1. Ensure you have Python installed on your machine.
2. Save the script to a `.py` file (e.g., `text_processing.py`).
3. Run the script using the command:

   ```bash
   python text_processing.py