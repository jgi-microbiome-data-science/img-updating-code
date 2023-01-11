mash dist -p 64 data/img.msh data/gtdb_paths.list -l \
| awk 'BEGIN{OFS=FS="\t"}NR==1{R=$1;Q=$2;D=$3}{if($2!=Q){print R,Q,D;R=$1;Q=$2;D=$3};if($3<D){R=$1;D=$3};Q=$2}END{print R,Q,D}' \
> data/mash_dist.tsv
