from snippet_compiler import compile_lean_file, print_stripped_compile_file
import os

EXAMPLE_FOLDER = "examples"

for file in os.listdir(EXAMPLE_FOLDER):
    if not file.endswith(".lean"):
        continue
    print(f"exporting file {file}...")
    print(file)
    name = os.path.splitext(file)[0]
    with open(os.path.join(EXAMPLE_FOLDER, file)) as file_io:
        first_line = file_io.readline()
    if first_line.startswith("prelude"):
        compile_lean_file(os.path.join(EXAMPLE_FOLDER, file), os.path.join(EXAMPLE_FOLDER, name + "_full.txt"))
    else:
        print_stripped_compile_file(os.path.join(EXAMPLE_FOLDER, file), False, os.path.join(EXAMPLE_FOLDER, name + "_diff.txt"))
        print_stripped_compile_file(os.path.join(EXAMPLE_FOLDER, file), True, os.path.join(EXAMPLE_FOLDER, name + "_full.txt"))
