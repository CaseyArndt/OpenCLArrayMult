#!/bin/bash
#SBATCH -J third
#SBATCH -A cs475-575
#SBATCH -p class
#SBATCH --gres=gpu:1
#SBATCH -o third.out
#SBATCH -e third.err
for s in 32 64 128 256
do
    for t in 1024 4096 16384 65536 262144 1048576 4194304 16777216
    do
    g++ -DNUM_ELEMENTS=$t -DLOCAL_SIZE=$s -o third third.cpp /usr/local/apps/cuda/10.1/lib64/libOpenCL.so.1.1 -lm -fopenmp
    ./third
    done
done