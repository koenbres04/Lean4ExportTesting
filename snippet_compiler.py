import os
import subprocess
import argparse
import shutil

EMPTY_OUTPUT_FILE = "output_empty.txt"

TEMP_LEAN_MODULE = "temp"
TEMP_OUTPUT_FILE = "temp_output.txt"

LEAN4EXPORT_FOLDER = "lean4export"


class PrintStream:
    def write(self, text: str):
        print(text, end="")

def compile_local_lean_module(module, output_file: str):
    subprocess.run(["lean", "-o", module + ".olean", module + ".lean"], cwd=LEAN4EXPORT_FOLDER)
    command_env = dict(os.environ)
    command_env["LEAN_PATH"] = "."
    subprocess.run(f"lake exe lean4export {TEMP_LEAN_MODULE} > {TEMP_OUTPUT_FILE}", shell=True, env=command_env, cwd=LEAN4EXPORT_FOLDER)
    os.remove(os.path.join(LEAN4EXPORT_FOLDER, module + ".olean"))
    os.rename(os.path.join(LEAN4EXPORT_FOLDER, TEMP_OUTPUT_FILE), output_file)

def compile_lean_file(input_file: str, output_file: str):
    temp_lean_file = os.path.join(LEAN4EXPORT_FOLDER, TEMP_LEAN_MODULE + ".lean")
    shutil.copy(input_file, temp_lean_file)
    compile_local_lean_module(TEMP_LEAN_MODULE, output_file)
    os.remove(temp_lean_file)


def print_stripped_compile_file(input_file: str, full: bool, output_file: str | None):
    if full and output_file is not None:
        compile_lean_file(input_file, output_file)
        return
    compile_lean_file(input_file, TEMP_OUTPUT_FILE)
    with open(TEMP_OUTPUT_FILE, encoding="UTF-8") as temp_stream:
        if full:
            while (data := temp_stream.read(1 << 16)) != "":
                print(data, end="")
        else:
            with open(EMPTY_OUTPUT_FILE, encoding="UTF-8") as base_stream:
                if output_file is None:
                    compare_streams(temp_stream, base_stream, PrintStream())
                else:
                    with open(output_file, "w") as output_stream:
                        compare_streams(temp_stream, base_stream, output_stream)
    os.remove(TEMP_OUTPUT_FILE)

def process_line(line: str):
    result = []
    for item in line.rstrip().split(" "):
        if all(x in "0123456789" for x in item):
            result.append(0)
        else:
            result.append(item)
    return tuple(result)

def lines_match(left: str, right: str) -> bool:
    return process_line(left) == process_line(right)


class StreamWindow:
    def __init__(self, stream, length: int):
        self.stream = stream
        self.lines = [stream.readline() for _ in range(length)]
    
    def step(self, num: int = 1):
        for _ in range(num):
            self.lines = self.lines[1:] + [self.stream.readline()]
    
    @property
    def first(self) -> str:
        return self.lines[0]


def compare_streams(new_stream, base_stream, output_stream, num_to_match_lines: int = 20, error_range: int = 10):
    line_counter = 0
    is_diff_mode = True
    base_window = StreamWindow(base_stream, num_to_match_lines)
    new_window = StreamWindow(new_stream, num_to_match_lines)
    while new_window.first != "":
        if not is_diff_mode:
            if not lines_match(base_window.lines[error_range], new_window.lines[error_range]):
                output_stream.write(f"\n@@ {line_counter} lines @@\n\n")
                base_window.step(error_range)
                line_counter = -error_range
                is_diff_mode = True
                continue
            base_window.step()
        else:
            if all(lines_match(base, new) for base, new in zip(base_window.lines, new_window.lines)):
                line_counter = 0
                is_diff_mode = False
                continue
            output_stream.write(("? " if line_counter < 0 else "+ ") + new_window.first)
        new_window.step()
        line_counter += 1
    if not is_diff_mode:
        output_stream.write(f"\n@@ {line_counter} lines @@\n")


# ensure the empty output file exists
if not os.path.exists(EMPTY_OUTPUT_FILE):
    print("creating empty output file...")
    temp_lean_file = os.path.join(LEAN4EXPORT_FOLDER, TEMP_LEAN_MODULE + ".lean")
    with open(temp_lean_file, "w"):
        pass
    compile_local_lean_module(TEMP_LEAN_MODULE, EMPTY_OUTPUT_FILE)
    os.remove(temp_lean_file)
    print("done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script for compiling lean files and extracting the new bits.")
    parser.add_argument("input")
    parser.add_argument("-f", "--full", action='store_true')
    parser.add_argument("-o", "--output")

    args = parser.parse_args()
    print_stripped_compile_file(args.input, args.full, args.output)
