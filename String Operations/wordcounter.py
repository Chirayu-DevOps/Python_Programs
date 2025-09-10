import argparse

# 1. Create parser
parser = argparse.ArgumentParser(description="Text File Word Counter")

# 👇 make sure argument name is 'file'
parser.add_argument("file", help="Name of the text file to read")

# 2. Parse arguments
args = parser.parse_args()

try:
    # 3. Open file in read mode
    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()

    # 4. Split text by spaces and count words
    words = content.split()
    word_count = len(words)

    # 5. Print result
    print(f"Total words in '{args.file}': {word_count}")

except FileNotFoundError:
    print(f"Error: File '{args.file}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
