import sys
import os
from PIL import Image, ImageOps


def main():
    # Check if the correct number of command-line arguments is provided
    check_arguments()

    # Extract input and output file names from command-line arguments
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    # Check input and output file extensions
    check_extensions(input_file_name, output_file_name)

    # Read the input image
    input_image = Image.open(input_file_name)

    # Resize and crop the input image to match the size of the shirt image
    edited_image = resize_and_crop(input_image)

    # Overlay the shirt image on the edited image
    overlay_shirt(edited_image)

    # Save the edited image to the output file
    edited_image.save(output_file_name)


def check_arguments():
    # Check if the number of command-line arguments is exactly 2
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def check_extensions(input_file, output_file):
    # Define the set of valid file extensions (case-insensitive)
    valid_extensions = {".jpg", ".jpeg", ".png"}

    # Get the lowercased extensions of the input and output files
    input_extension = os.path.splitext(input_file)[1].lower()
    output_extension = os.path.splitext(output_file)[1].lower()

    # Check if the output file extension is valid
    if output_extension not in valid_extensions:
        sys.exit("Invalid output")
    # Check if the input and output file extensions match
    elif input_extension != output_extension:
        sys.exit("Input and output have different extensions")


def resize_and_crop(input_image):
    # Open the shirt image to get its size
    shirt = Image.open("shirt.png")
    size = shirt.size

    # Resize and crop the input image to match the size of the shirt image
    edited_image = ImageOps.fit(input_image, size)

    return edited_image


def overlay_shirt(edited_image):
    # Open the shirt image
    shirt = Image.open("shirt.png")
    # Overlay the shirt image on the edited image
    edited_image.paste(shirt, shirt)


if __name__ == "__main__":
    main()
