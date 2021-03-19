import sys  # Module that interacts strongly with the Python interpreter
script, encoding, error = sys.argv  # List of command line arguments passed to the script. First = file name


def main(language_file, encoding, errors):
    line = language_file.readline() # Reads single line of file

    if line:
        print_line(line, encoding, errors) # If a line exists, calls print_line function to print the raw bytes and encoded bytes
        return main(language_file, encoding, errors) # Recursively calls main() function until no more lines exist within the file

def print_line(line, encoding, errors):
    next_lang = line.strip() # Cleans whitespace before/after
    raw_bytes = next_lang.encode(encoding, errors=errors) # Encodes string into bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) # Decodes raw bytes into specified encoding

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

# 'DBES' when working with strings
# - Decode Bytes. ex: raw_bytes.decode()
# - Encode strings. ex: utf_string.encode()