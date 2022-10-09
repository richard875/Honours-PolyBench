import os
import shutil
import pathlib
from datetime import datetime
from test_list import get_all_files
from helper.console_colors import Bcolors

# standard size is large size
RUNTIME_OUTPUT_FOLDER = "compiled"
RESULTS_OUTPUT_FOLDER = "results"
UTILITIES_FOLDER = f"{pathlib.Path(__file__).parent.resolve()}/polybench-c-4.2.1-beta/utilities"
UTILITIES_FILE = "/polybench.c"
INPUT_SIZE = {
    "standard": ["", Bcolors.BOLD],
    "mini": ["-DMINI_DATASET", Bcolors.OKCYAN],
    "small": ["-DSMALL_DATASET", Bcolors.OKGREEN],
    "medium":["-DMEDIUM_DATASET", Bcolors.OKBLUE],
    "large": ["-DLARGE_DATASET", Bcolors.WARNING],
    # "extralarge": ["-DEXTRALARGE_DATASET", Bcolors.FAIL],
}

def main():
    isdir = os.path.isdir(RUNTIME_OUTPUT_FOLDER)
    isOutputdir = os.path.isdir(RESULTS_OUTPUT_FOLDER)
    if not isdir: os.mkdir(RUNTIME_OUTPUT_FOLDER)
    if not isOutputdir: os.mkdir(RESULTS_OUTPUT_FOLDER)

    all_files = get_all_files()

    date_time_now = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    output_file = open(f"{RESULTS_OUTPUT_FOLDER}/output-file-{date_time_now}.txt", "w")

    print("Executing all files...")
    print("=======================================================")
    output_file.write("Executing all files...\n")
    output_file.write("=======================================================\n")

    for file in all_files:
        name = file[0]
        path = file[1]

        print(f"{name} ->")
        output_file.write(f"{name} ->\n")

        for size in INPUT_SIZE:
            compile_file = f"gcc -O3 -I {UTILITIES_FOLDER} -I {path} {UTILITIES_FOLDER}{UTILITIES_FILE} {path}/{name}.c -DPOLYBENCH_TIME {INPUT_SIZE[size][0]} -o compiled/{name}_{size}"
            execute_file = f"./compiled/{name}_{size}"

            os.system(compile_file)
            so = os.popen(execute_file).read().strip()
            
            print(f"Executed with input size {INPUT_SIZE[size][1]}{size}: {so}s{Bcolors.ENDC}")
            output_file.write(f"Executed with input size {size}: {so}s\n")
        
        print("=======================================================")
        output_file.write("=======================================================")
    
    isdir = os.path.isdir(RUNTIME_OUTPUT_FOLDER)
    if isdir: shutil.rmtree(RUNTIME_OUTPUT_FOLDER, ignore_errors=True)
    output_file.close()

if __name__ == "__main__":
    main()