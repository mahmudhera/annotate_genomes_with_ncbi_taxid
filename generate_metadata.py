import os
import pandas as pd

# things that are hard-coded:
# 1. output_filename
# 2. all_genomes_filename
# 3. genome_name_to_taxid_filename

if __name__ == '__main__':
    output_filename = 'metadata.tsv'
    output_file = open(output_filename, 'w')
    output_file.write('genome_ID\tOTU\tNCBI_ID\tnovelty_category\n')

    all_genomes_filename = 'scientific_name_to_genome_name.csv'
    all_genomes_df = pd.read_csv(all_genomes_filename, sep='\t')
    scientific_name_to_genome_name = dict(zip(all_genomes_df['scientific_name'], all_genomes_df['genome_name']))
    genome_name_to_scientific_name = dict(zip(all_genomes_df['genome_name'], all_genomes_df['scientific_name']))

    scientific_name_to_taxid_filename = 'list_of_taxids'
    scientific_name_to_taxid_df = pd.read_csv(scientific_name_to_taxid_filename, sep='\t', header=None)
    scientific_name_to_taxid_df.columns = ['genome_name', 'taxid']
    scientific_name_to_taxid = dict(zip(scientific_name_to_taxid_df['genome_name'], scientific_name_to_taxid_df['taxid']))

    OTU = 1
    num_genomes_not_in_taxid_list = 0
    for genome_name in genome_name_to_scientific_name.keys():
        try:
            output_file.write(genome_name + '\t' + str(OTU) + '\t' + str(int(scientific_name_to_taxid[ genome_name_to_scientific_name[genome_name] ])) + '\t' + 'known_strain\n')
        except:
            num_genomes_not_in_taxid_list += 1
            continue
        OTU += 1

    output_file.close()
    print('Number of genomes not in taxid list: ' + str(num_genomes_not_in_taxid_list))