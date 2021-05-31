import os

work_sizes = [8, 16, 32, 64, 128, 256, 512]
elements = [1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216]

if __name__ == '__main__':


    for s in work_sizes:
        for t in elements:
            cmd = f"g++ -DNUM_ELEMENTS={t} -DLOCAL_SIZE={s} -o second second.cpp /usr/local/apps/cuda/10.1/lib64/libOpenCL.so.1.1 -lm -fopenmp"
            os.system(cmd)
            cmd = "./second"
            os.system(cmd)