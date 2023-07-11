import csv
import sys


def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Check if the first command-line argument is not a CSV file
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Extract input and output file names from command-line arguments
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    # Read data from input file
    students = read_file(input_file_name)

    # Process the data to split the "name" field into "first" and "last" fields
    cleaned_list = clean_file(students)

    # Write the cleaned data to the output file
    write_file(output_file_name, cleaned_list)


def read_file(input_file):
    try:
        students = []
        # Open the input CSV file and create a CSV reader object
        with open(input_file) as file:
            reader = csv.DictReader(file)
            # Read each row (student) from the CSV file and append it to the list
            for student in reader:
                students.append(student)

        return students

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file_name}")


def clean_file(students):
    # Process each student's record (dictionary) in the list
    for student in students:
        # Extract the "name" field and split it into "first" and "last" fields
        full_name = student["name"]
        last_name, first_name = full_name.split(", ")
        # Add "first" and "last" fields to the student's record and remove "name" field
        student["last"] = last_name
        student["first"] = first_name
        del student["name"]

    return students


def write_file(output_file, students):
    # Define the header for the output CSV file
    header = ["first", "last", "house"]
    # Open the output CSV file and create a CSV writer object
    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        # Write the header row to the output file
        writer.writeheader()
        # Write the data (students' records) to the output file
        writer.writerows(students)


# Check if this script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the program
    main()
