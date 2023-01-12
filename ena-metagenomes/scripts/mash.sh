#!/bin/bash -l

#SBATCH --constraint haswell
#SBATCH --qos=genepool
#SBATCH -A pkimg
#SBATCH -n 1
#SBATCH -t 12:00:00
#SBATCH --mem 100G

module load python
source activate snayfach

mash dist -p 64 data/img.msh data/gtdb_paths.list -l \
| awk 'BEGIN{OFS=FS="\t"}NR==1{R=$1;Q=$2;D=$3}{if($2!=Q){print R,Q,D;R=$1;Q=$2;D=$3};if($3<D){R=$1;D=$3};Q=$2}END{print R,Q,D}' \
> data/mash_dist.tsv
