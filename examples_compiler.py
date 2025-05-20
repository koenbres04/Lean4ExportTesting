from snippet_compiler import print_stripped_compile_file
import os

EXAMPLE_FOLDER = "examples"

for file in os.listdir(EXAMPLE_FOLDER):
    if not file.endswith(".lean"):
        continue
    print(f"exporting file {file}...")
    name = os.path.basename(file)
    print_stripped_compile_file(os.path.join(EXAMPLE_FOLDER, file), False, os.path.join(EXAMPLE_FOLDER, name + "_diff.txt"))
    print_stripped_compile_file(os.path.join(EXAMPLE_FOLDER, file), True, os.path.join(EXAMPLE_FOLDER, name + "_full.txt"))
        