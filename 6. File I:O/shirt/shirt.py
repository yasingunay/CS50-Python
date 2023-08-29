import sys
import os
from PIL import Image, ImageOps


def main():
    extensions = [".jpg", ".jpeg", ".png"]
    input_file, output_file = sys.argv[1], sys.argv[2]

    # Check the user specifies exactly two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check the input’s and output’s names ends in .jpg, .jpeg, or .png, case-insensitively
    elif not input_file.lower().endswith(tuple(extensions)):
        sys.exit("Invalid input")

    elif not output_file.lower().endswith(tuple(extensions)):
        sys.exit("Invalid input")

    # Check the input’s name has the same extension as the output’s name
    elif not have_same_extension(sys.argv[1], sys.argv[2]):
        sys.exit("Input and output have different extensions")

    else:
        open_and_paste_image()


def get_extension(filename):
    try:
        # Get the file extension from the filename
        # Other solution: _, _, ext = filename.rpartition(".")
        _, ext = os.path.splitext(filename)
        return ext
    except ValueError:
        sys.exit("Invalid input")


def have_same_extension(str1, str2):
    # Get the extensions from both strings
    ext1 = get_extension(str1)
    ext2 = get_extension(str2)

    # Compare the extensions
    return ext1 == ext2


def open_and_paste_image():
    # Open the image passed as a command-line argument
    try:
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open the shirt image (assumed to be named "shirt.png")
    shirt = Image.open("shirt.png")

    # Get the size of the shirt image
    size = shirt.size

    # Resize the muppet image to match the size of the shirt
    muppet = ImageOps.fit(muppet, size)

    # Paste the shirt image onto the muppet image
    muppet.paste(shirt, shirt)

    # Get the output file path from command-line arguments
    output_path = sys.argv[2]

    # Save the modified muppet image to the specified output path
    muppet.save(output_path)


if __name__ == "__main__":
    main()
