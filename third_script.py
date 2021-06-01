import os

work_sizes = [32, 64, 128, 256]
elements = [1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216]

if __name__ == '__main__':


    for s in work_sizes:
        for t in elements:
            cmd = f"g++ -DNUM_ELEMENTS={t} -DLOCAL_SIZE={s} -o third third.cpp /usr/local/apps/cuda/10.1/lib64/libOpenCL.so.1.1 -lm -fopenmp"
            os.system(cmd)
            cmd = "./third"
            os.system(cmd)