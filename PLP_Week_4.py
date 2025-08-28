#File Read & Write Challenge 🖋️:
def modify_content(text):
    """Reads a string, returns a modified string."""
    lines = text.splitlines()
    modified_lines = []
    for number, line in enumerate(lines, 1):
        modified_lines.append(f"{number}, {line}")
    return '\n'.join(modified_lines)

# The main program function

def main():
# The Error Handling Lab 🛠️:
    
    filename = input("Enter the name of the file to read: ")
    
    try:
        with open(filename, 'r') as file:
            original_content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied. Cannot read '{filename}.")
        return
    except OSError as e:
        print(f"Error: Could not read the file: {e}.")
        return

    print("Now modify content of the succefully read file...")

    new_content = modify_content(original_content)
    output_filename = "modified_" + filename

    try:
        with open(output_filename, 'w') as file:
            file.write(new_content)
        print(f"Modified content written to your '{output_filename}")
    except OSError as e:
        print(f"Error: Could not write to the file: {e}.")

    print("Congratulations! The program completed successfully.")

if __name__ == "__main__":
    main()   

