import os

# Get the current working directory
current_path = os.getcwd()

# Print the current working directory
print(current_path)

# Now, if you want to add a filename to this path, you can do the following:
file_path = os.path.join(current_path, '/preprocessing/filename.csv')
print(file_path)