import os

# meant to run on the GPU machine
genomes_directory_names = '/scratch/mbr5797/genomes_extracted_from_kegg'
output_filename = 'genome_to_id.tsv'
metadata_filename = 'metadata.tsv'

if __name__ == '__main__':
    # open metadata, read the column genome_ID, store it in a list
    genome_ids = []
    with open(metadata_filename, 'r') as metadata_file:
        for line in metadata_file:
            genome_ids.append(line.split('\t')[0])

    # open output file
    with open(output_filename, 'w') as output_file:
        # for each genome_ID, generate the fasta filename as: genome_directory_names/genome_ID/genome_ID.fasta, write it to the output file
        for genome_id in genome_ids[1:]:
            output_file.write(genome_id + '\t' + genomes_directory_names + '/' + genome_id + '/' + genome_id + '.fasta\n')