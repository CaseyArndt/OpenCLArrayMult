#!/bin/bash
#SBATCH -J first
#SBATCH -A cs475-575
#SBATCH -p class
#SBATCH --gres=gpu:1
#SBATCH -o first.out
#SBATCH -e first.err
for s in 8 16 32 64 128 256 512
do
    for t in 1024 4096 16384 65536 262144 1048576 4194304 16777216
    do
    g++ -DNUM_ELEMENTS=$t -DLOCAL_SIZE=$s -o first first.cpp /usr/local/apps/cuda/10.1/lib64/libOpenCL.so.1.1 -lm -fopenmp
    ./first
    done
done