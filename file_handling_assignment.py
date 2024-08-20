

def create_and_write_file(filename):
    """Create a file and write initial user data."""
    try:
        with open(filename, 'w') as file:
            file.write("UserID,Name,Email\n")
            file.write("1,Alice Harper,alice.harper@example.com\n")
            file.write("2,David Kim,david.kim@example.com\n")
            file.write("3,Sophia Martinez,sophia.martinez@example.com\n")
        print("Initial data written to file successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error creating or writing to file: {e}")
    finally:
        print("File creation and writing attempt completed.")

def read_and_display_file(filename):
    """Read and display the contents of the file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nCurrent File Content:")
            print(content)
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading file: {e}")
    finally:
        print("File reading attempt completed.")

def append_to_file(filename):
    """Append additional user data to the file."""
    try:
        with open(filename, 'a') as file:
            file.write("4,Emily Nguyen,emily.nguyen@example.com\n")
            file.write("5,James Parker,james.parker@example.com\n")
            file.write("6,Linda Scott,linda.scott@example.com\n")
        print("Additional data appended to file successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("File appending attempt completed.")

def main():
    filename = 'user_data.txt'
    
    # Create and write initial data
    create_and_write_file(filename)
    
    # Read and display current data
    read_and_display_file(filename)
    
    # Append more data
    append_to_file(filename)
    
    # Read and display updated data
    read_and_display_file(filename)

if __name__ == "__main__":
    main()
