# mc-md

This is a simple repo for running a hybrid MC-MD ([Monte Carlo](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm) + [Molecular Dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics)) run for the [Cantor alloy](https://briandcolwell.com/what-are-high-entropy-alloys-heas-the-cantor-alloy-four-core-effects-hea-properties-and-more-a-complete-guide-to-revolutionary-multi-element-materials-for-beginners/) (CoNiCrFeMn).

To run the given input script, follow the steps below:

## Download the repository

You only need to do this once! You can use `git` to put this into Palmetto (or `wget` as well, but `git` is my preferred):

```bash
git clone https://github.com/jwjeffr/mc-md.git
```

After you clone the repository, you can check that you now have the folder by typing:

```bash
ls
```

You should see `mc-md` as an available directory. 

## Enter the repository

```bash
cd mc-md/
```

## Submit the job

On Palmetto, submit a batch job using my [LAMMPS](https://en.wikipedia.org/wiki/LAMMPS) executable:

```bash
sbatch mc.slurm
```

If you open `mc.slurm`, you'll see where the LAMMPS executable is defined. By default, I've included my own LAMMPS executable, which any Palmetto user can access. You can change this to your own executable if you have one. The potential in this repo is from the NIST entry [here](https://www.ctcms.nist.gov/potentials/entry/2018--Choi-W-M-Jo-Y-H-Sohn-S-S-et-al--Co-Ni-Cr-Fe-Mn/)

## Monitor the job

You can run the following command to monitor any submitted jobs:

```bash
squeue -u $USER
```

`USER` is just a variable automatically defined for you, and should just be your username. You can check this by running ```echo $USER``` to print out its value.

You should see a table with the submitted job. If it's running, great! It will probably sit in the queue, though.

Once it actually starts running, you can go back to the `mc-md` directory and type `ls` to see any new files created. You should see some new files

- `log.lammps`, which is a LAMMPS log file.
- `mc.dump`, which is the simulation output file containing all of the positions of the atoms
- `slurm-xxxxxx.out`, where the `x`'s are the job ID.

You can preview any of these files by typing `less file-name`, and can exit the view by pressing `Q`.

## More generally

These commands are all just standard Linux commands. There are a huge amount of tutorials online for this kind of thing - play around with it! But, make sure you leave the `mc-md` directory before you mess with anything:

```bash
cd ..
```

which takes you to the directory above `mc-md`, which should be your home directory. You don't want to mess with the simulation output while the simulation is running!