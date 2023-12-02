import os

def run_solve_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file == "solve.py":
                file_path = os.path.join(root, file)
                exec(open(file_path).read(), {'__file__': file_path})

# Specify the root directory where you want to start searching
root_directory = "/Users/michiel/SOURCE/CC_AI/AoC/2023"

# Call the function to run all solve.py files
run_solve_files(root_directory)
