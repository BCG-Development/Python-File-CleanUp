import os

def clean_directory(directory):
    """
    Clean up all files in the specified directory.

    :param directory: The path to the directory to clean up.
    """
    os.chdir(directory)
    all_files = os.listdir()

    for file in all_files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

def main():
    """
    Main function to ask the user for the directory path.
    """
    directory = input("Enter the path to the directory you want to clean up: ")

    # Validate that the entered directory exists
    if os.path.exists(directory) and os.path.isdir(directory):
        try:
            clean_directory(directory)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid directory path. Please enter a valid path.")

if __name__ == "__main__":
    main()
