#!/bin/bash

#SBATCH --job-name mc
#SBATCH --cpus-per-task 16
#SBATCH --mem 64gb
#SBATCH --time 12:00:00

LMP_PATH=/home/jwjeffr/software_slurm/lammps-2Aug2023/build/lmp

"${LMP_PATH}" -in mc.in
