import os

genomes_directory_names = '/scratch/mbr5797/genomes_extracted_from_kegg'

if __name__ == '__main__':
    directory_names = [name for name in os.listdir(genomes_directory_names) if os.path.isdir(os.path.join(genomes_directory_names, name))]
    with open('sc_names.txt', 'w') as f:
        for directory_name in directory_names[:10]:
            genome_file_name = os.path.join(genomes_directory_names, directory_name, directory_name+'.fasta')
            with open(genome_file_name, 'r') as g:
                first_line = g.readline()
                first_line = first_line.strip()
                print(first_line.split(' '))
            f.write(first_line+'\n')