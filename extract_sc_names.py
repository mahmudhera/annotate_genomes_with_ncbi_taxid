import os
import random

genomes_directory_names = '/scratch/mbr5797/genomes_extracted_from_kegg'

if __name__ == '__main__':
    directory_names = [name for name in os.listdir(genomes_directory_names) if os.path.isdir(os.path.join(genomes_directory_names, name))]
    random.shuffle(directory_names)
    f2 = open('scientific_name_to_genome_name.csv', 'w')
    f2.write('scientific_name\tgenome_name\n')
    with open('scientific_names.txt', 'w') as f:
        for directory_name in directory_names:
            genome_file_name = os.path.join(genomes_directory_names, directory_name, directory_name+'.fasta')
            with open(genome_file_name, 'r') as g:
                first_line = g.readline()
                first_line = first_line.strip()
            sc_name = ' '.join(first_line.split(' ')[2:4])
            print(sc_name + ' extracted from ' + directory_name)
            f.write(sc_name + '\n')
            f2.write(sc_name + '\t' + directory_name + '\n')
    f2.close()