import time

from FileOrganizer import FileOrganizer

def main() -> None:
    """Main function to run the File Organizer program."""
    try:
        file_organiser = FileOrganizer()
        file_organiser.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Exiting program in 10 seconds...")
        time.sleep(10)
        exit(1)

if __name__ == "__main__":
    main()