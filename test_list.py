import pathlib

ROOT_FOLDER = "polybench-c-4.2.1-beta"
MAIN_FOLDERs = ["datamining", "linear-algebra", "medley", "stencils"]
LINEAR_ALGEBRA_FOLDERs = ["blas", "kernels", "solvers"]

ALL_FILES = {
    "datamining": ["correlation", "covariance"],
    "blas": ["gemm", "gemver", "gesummv", "symm", "syr2k", "syrk", "trmm"],
    "kernels": ["2mm", "3mm", "atax", "bicg", "doitgen", "mvt"],
    "solvers": ["cholesky", "durbin", "gramschmidt", "lu", "ludcmp", "trisolv"],
    "medley": ["deriche", "floyd-warshall", "nussinov"],
    "stencils": ["adi", "fdtd-2d", "heat-3d", "jacobi-1d", "jacobi-2d", "seidel-2d"],
}

def get_all_files():
    all_files = []
    for folder in MAIN_FOLDERs:
        if folder == "linear-algebra":
            for subfolder in LINEAR_ALGEBRA_FOLDERs:
                for file in ALL_FILES[subfolder]:
                    all_files.append([file, f"{pathlib.Path(__file__).parent.resolve()}/{ROOT_FOLDER}/{folder}/{subfolder}/{file}"])
        else:
            for file in ALL_FILES[folder]:
                    all_files.append([file, f"{pathlib.Path(__file__).parent.resolve()}/{ROOT_FOLDER}/{folder}/{file}"])
        
    return [all_files[0]]