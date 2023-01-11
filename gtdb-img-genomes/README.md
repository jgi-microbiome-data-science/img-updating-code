# Code to compare GTDB to IMG genomes

### Follow the commands in the notebook to:  

- download metadata for gtdb  
- download the latest gtdb genomes from ncbi 
- create a mash sketch of IMG genomes
- compare GTDB genomes to IMG sketch 

...that's it! at this point you can:

- select genomes in GTDB without a close match to IMG (min mash distance > 0.05)
- you can also prioritize isolates (see: ncbi_genome_category field from data/bac120_metadata_r207.tsv and data/ar53_metadata_r207.tsv)

### External requirements

- mash (https://github.com/marbl/Mash)
- parallel (https://anaconda.org/conda-forge/parallel)


### Previously computed output

- mash_dist.tsv: <img_taxon_id>, <ncbi_taxon_id>, <mash_distance>
- gtdb_r207_metadata.tsv: metadata for GTDB genomes

Note: GTDB and NCBI genomes do not perfectly match

- GTDB genome id: GB_GCA_017649845.1; NCBI genome id: GCA_017649845.1
- GTDB genome id: RS_GCF_000007665.1; NCBI genome id: GCA_000007665.1 
