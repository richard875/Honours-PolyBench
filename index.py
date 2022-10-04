import os
from test_list import get_all_files

# cmd1 = "gcc -O3 -I utilities -I linear-algebra/kernels/atax utilities/polybench.c linear-algebra/kernels/atax/atax.c -DPOLYBENCH_TIME -o atax_time"
# cmd2 = "./atax_time"
# os.system(cmd1)
# so = os.popen(cmd2).read()
# print(so)


all_files = get_all_files()

for file in all_files:
    print(file, end="\n")