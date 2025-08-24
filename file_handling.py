# Step 1: Create input.txt with at least five lines of text
with open("input.txt", "w") as f:
    f.write("Python is a powerful programming language.\n")
    f.write("It is widely used for web development.\n")
    f.write("Data science and machine learning are popular fields.\n")
    f.write("Python has a simple syntax.\n")
    f.write("It is easy to learn and use.\n")

# Step 2: Read contents of input.txt
with open("input.txt", "r") as f:
    content = f.read()

# Step 3: Count the number of words
word_count = len(content.split())

# Step 4: Convert all text to uppercase
upper_content = content.upper()

# Step 5: Write processed text and word count to output.txt
with open("output.txt", "w") as f:
    f.write(upper_content)
    f.write(f"\nWORD COUNT: {word_count}\n")

# Step 6: Print success message
print("output.txt has been created successfully.")