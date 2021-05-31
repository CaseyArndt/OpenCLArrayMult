import os

work_sizes = [8, 16, 32, 64, 128, 256, 512]
elements = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]

if __name__ == '__main__':


    for s in work_sizes:
        for t in elements:
            cmd = f"g++ -DNUM_ELEMENTS={t} -DLOCAL_SIZE={s} -o first first.cpp /usr/local/apps/cuda/10.1/lib64/libOpenCL.so.1.1 -lm -fopenmp"
            os.system(cmd)
            cmd = "./first"
            os.system(cmd)