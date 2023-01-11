wget 'https://www.ebi.ac.uk/ena/portal/api/links/taxon?accession=408169&result=analysis&download=true&subtree=true&offset=0' -O data/lists/accessions_1.tsv
wget 'https://www.ebi.ac.uk/ena/portal/api/links/taxon?accession=408169&result=analysis&download=true&subtree=true&offset=100000' -O data/lists/accessions_2.tsv
wget 'https://www.ebi.ac.uk/ena/portal/api/search?result=analysis&query=center_name=EMG&offset=0' -O data/lists/accessions_3.tsv
wget 'https://www.ebi.ac.uk/ena/portal/api/search?result=analysis&query=center_name=EMG&offset=100000' -O data/lists/accessions_4.tsv

cat /dev/null > data/lists/accessions_all.tsv
sed 1d data/lists/accessions_1.tsv | cut -f1 >> data/lists/accessions_all.tsv
sed 1d data/lists/accessions_2.tsv | cut -f1 >> data/lists/accessions_all.tsv
sed 1d data/lists/accessions_3.tsv | cut -f1 >> data/lists/accessions_all.tsv
sed 1d data/lists/accessions_4.tsv | cut -f1 >> data/lists/accessions_all.tsv

sort -u data/lists/accessions_all.tsv > data/lists/accessions_unique.tsv

module load parallel
cat data/lists/accessions_unique.tsv | sort -R | parallel "if [ ! -f data/xml/analyses/{} ]; then python scripts/fetch_analysis_xml.py {} &> log/{}; fi"

python scripts/parse_analysis_xml.py

python scripts/load_analysis_xml.py
