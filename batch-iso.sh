T=$1
ps=( 0.25 0.5 0.75 1.0 1.5 2.5 3.0)

for p in ${ps[@]}; do
    mpirun -np 4 ~/lammps/src/lmp_mpi -in scripts/isobars.lmp -v rho 0.05 -v T $T -v P $p
done

