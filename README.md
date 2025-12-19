# mc-md

This is a simple repo for running a hybrid MC-MD ([Monte Carlo](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm) + [Molecular Dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics)) run for the [Cantor alloy](https://briandcolwell.com/what-are-high-entropy-alloys-heas-the-cantor-alloy-four-core-effects-hea-properties-and-more-a-complete-guide-to-revolutionary-multi-element-materials-for-beginners/) (CoNiCrFeMn).

On Palmetto, submit a batch job using my [LAMMPS](https://en.wikipedia.org/wiki/LAMMPS) executable:

```bash
sbatch mc.slurm
```

If you open `mc.slurm`, you'll see where the LAMMPS executable is defined. You can change this to your own executable if you have one.