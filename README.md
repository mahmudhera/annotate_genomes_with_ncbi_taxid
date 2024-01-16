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

# TODO
There are still some genome names that do not have a tax id associated with them. These names are in the file `genome_names_to_exclude`. What we need to do is: we must not use these in the simulations. Simple!!

## What to do next?
Next, we need to create the following two files:

1. metadata.tsv
1. genome_to_id.tsv

### metadata.tsv
This is a tab separated file, with four fields:
1. genome_ID -- user given ID -- we will just use 3 digit name
1. OTU -- 1,2,3,4 etc.
1. NCBI_ID -- this is obtained from the file `list_of_taxids`
1. novelty_category -- this is always set as `known_strain`

### genome_to_id.tsv
This is easy. Also a tab separated file. There are two fields:
1. genome_ID -- we will again use the 3 digit name in the KEGG database
1. file_path -- this is the path to the fasta file

## Summary
1. run `extract_sc_names.py`. This will generate `scientific_names.txt`, which is a list of all scientific names of all organisms that we have in the KEGG database. Do not forget to set the path -- they are hardcoded. This will also generate the file `scientific_name_to_genome_name.csv`. The explanation is self.
1. run `cat scientific_names.txt | taxonkit name2taxid > list_of_taxids`. The output file will contain scientific name in column 1, and taxid in column 2.
1. run `extract_names_with_no_taxid.py > genome_names_to_exclude`. This will generate a list of genome 3 digit names to not use.
1. run `generate_genome_to_id.py`. This will generate a file named `genome_to_id.tsv` as explained above. This will take all genomes in our KEGG database list of genomes, skip the genomes that are to be excluded, and store the info of the rest (genomes for which, a valid taxid was obtained successfully).
1. run `generate_metadata.tsv`. This will generate the metadata.tsv file, as explained above. This will also only use the genomes for which, a valid taxid is available, and skip the others.

Important info to note:
1. scientific name to 3-digit name and vice versa: `scientific_name_to_genome_name.csv`
1. scientific name to taxid: `list_of_taxids`
1. 3-digit names to exclude: `genome_names_to_exclude`