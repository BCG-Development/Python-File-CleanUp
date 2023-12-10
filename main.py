import os
import glob

def clean_directory(directory):
    """
    Clean up all files in the specified directory.

    :param directory: The path to the directory to clean up.
    """
    os.chdir(directory)
    all_files = glob.glob('*')

    for file in all_files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

def main():
    """
    Main function to interactively ask the user which directory to clean up.
    """
    print("Select an option:")
    print("1. Clean up temporary files directory")
    print("2. Clean up downloads directory")
    
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        temp_directory = input("Enter the path to the temporary files directory: ")
        clean_directory(temp_directory)
    elif choice == '2':
        downloads_directory = input("Enter the path to the downloads directory: ")
        clean_directory(downloads_directory)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
