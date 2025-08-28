# week4_file_handling.py

def read_and_write_file(input_filename, output_filename):
    """
    Reads content from input file, modifies it,
    and writes to output file.
    """
    try:
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Example modification: Convert all text to uppercase
        modified_content = content.upper()

        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File '{output_filename}' created successfully with modified content.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print("Error: Unable to read or write file.")


def main():
    # Ask the user for a filename
    input_filename = input("Enter the filename to read: ").strip()
    output_filename = "modified_" + input_filename

    read_and_write_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
