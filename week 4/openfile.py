#QUESTION 1: Create a program that reads a file and writes a modified version to a new file.

file = open('Newfile.txt', 'w')
file.write("Hello, My Name is Maryjane,\n")
file = open('Newfile.txt', 'a')
file.write("I am an Aspiring software developer.\n")

# Now read the content from input.txt/ Reading operation
with open("Newfile.txt", "r") as file:
    content = file.read()

# Modify the content (e.g., make it uppercase)
modified_content = content.upper()

# Write the modified content into a new file
with open("schoolfile.txt", "w") as new_file:
    new_file.write(modified_content)

print("File has been read, modified, and saved successfully")

                                      
#QUESTION 2: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    # Ask user for a filename
    filename = input("Enter the filename: ")

    # Try to open and read it
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("Error: Hey BESTIE,the file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")