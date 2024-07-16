def file_copy(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read()
    except FileNotFoundError:
        return "Source file not found."
    except IOError:
        return "Error reading source file."

    try:
        with open(destination, 'w') as dest_file:
            dest_file.write(content)
    except IOError:
        return "Error writing to destination file."

    return "File copied successfully."

# Example usage:
source_file = "source.txt"
destination_file = "destination.txt"
print(file_copy(source_file, destination_file))
