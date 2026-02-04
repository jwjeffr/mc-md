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

If you get a weird error about newlines, you probably have an encoding error related to differences between how Mac/Windows/Unix deals with things. You can fix it by converting the file:

```bash
dos2unix mc.slurm
```

and then resubmitting the `sbatch` command.

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

# Analyzing the run

Now that we have a generated `mc.dump` after running the `mc.in` file, we want to analyze it. We can do this with a variety of tools, but the most common is using Python due to its large ecosystem of third-party tools.

We'll use some tools that are popular for most Python users (`numpy`, `matplotlib`), OVITO's library to read in the file for us (`ovito`), as well as our in-house plugin to compute short-range order parameters (`cowley-sro-parameters`).

## Setting up the environment

You'll want to update your repository on Palmetto to grab the new files. You can do this with:

```bash
git pull origin main
```

which will merge any changes, which, in this case, are the new analysis files. Make sure you're in the right directory!

Then, we'll want to install the packages above in an isolated environment in what is called a virtual environment. There are a lot of reasons you'd want to do this in general. I'd encourage watching this video [here](https://www.youtube.com/watch?v=Y21OR1OPC9A) to motivate it.

To set up the virtual environment:

```bash
module add anaconda3
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The respective commands:
- Include the `anaconda3` module on Palmetto, which contains the `python` executable
- Create the virtual environment in the `venv` folder
- Activate the virtual environment
- Install the corresponding packages

`requirements.txt` is just a text file with the packages pinned to specific versions.

## Running the analysis script

After setting up the environment, run:

```bash
python sro-parameters.py
```

which will generate an `sro.pdf` file containing a figure with the SRO parameters. Grab this off of Palmetto onto your local machine, and take a look! The file is included in the GitHub repo as a `.png`:

***PLACEHOLDER***

Each cell in the colormap represents a pair of atom types. E.g., the Cr-Cr cell is the most strongly negative, meaning that the Cr atoms segregate with one another, which is consistent with what the run looks like in OVITO.

Take a look at the contents of the `sro-parameters.py` script, and try to understand what each line is doing. Any choice of LLM (like GPT) is great for breaking down these scripts line by line.