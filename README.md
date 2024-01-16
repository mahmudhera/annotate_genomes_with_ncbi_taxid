# annotate_genomes_with_ncbi_taxid
To use camisim with the genomes we downloaded from KEGG, it is important to know the NCBI taxid of all these genomes. In this repo, we will do this.

Directory structure of the genomes:

```
genomes_extracted_from_kegg
|
|----| genome_name1
|---------| genome_name1.fasta
|---------| genome_name1_mapping.csv
|
|----| genome_name2
|---------| genome_name2.fasta
|---------| genome_name2_mapping.csv
.
.
.
```

## Step 1
The python file will
1. go into each directory
1. extract the scientific name
1. write the scientific name in a file named `names.txt`

## Step 2
1. We will use `taxonkit` to get the taxids using the following command:
```
cat names.txt | taxonkit name2taxid
```

## Installation tips
1. python dependencies: None
1. taxonkit is installed here on the GPU machine: `/home/grads/mbr5797/taxonkit`