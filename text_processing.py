# Define the input text
input_text = [
    "I am an African\n",
    "I cherished my region\n",
    "I am from Nigeria\n",
    "I study with plp\n",
    "I am a software developer\n"
]

# Write to input.txt
with open("input.txt", "w") as file:
    file.writelines(input_text)

# Read input.txt and process content
with open("input.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    uppercase_content = content.upper()

# Write processed content to output.txt with error handling
try:
    with open("output.txt", "w") as file:
        file.write("Word Count: " + str(word_count) + "\n")
        file.write(uppercase_content)
    print("New file has been created SUCCESSFULLY")
except Exception as e:
    print(f"Error: {e}")

# Read and display output.txt
try:
    with open("output.txt", "r") as file:
        output_content = file.read()
        print("\nContent of output.txt:")
        print(output_content)
except FileNotFoundError:
    print("Error: output.txt not found.")
except IOError:
    print("Error: Could not read from the output file.")