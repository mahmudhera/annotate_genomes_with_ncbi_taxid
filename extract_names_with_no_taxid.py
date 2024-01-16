import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('scientific_name_to_genome_name.csv', sep='\t')
    scientific_name_list = df['scientific_name'].tolist()
    genome_name_list = df['genome_name'].tolist()
    sc_name_to_ge_name = {}
    for scientific_name, genome_name in list( zip(scientific_name_list, genome_name_list) ):
        sc_name_to_ge_name[scientific_name] = genome_name

    df = pd.read_csv('list_of_taxids', sep='\t', header=None)
    df.columns = ['scientific_name', 'taxid']
    for scientific_name, taxid in list( zip(df['scientific_name'].tolist(), df['taxid'].tolist()) ):
        if str(taxid) == 'nan':
            print(sc_name_to_ge_name[scientific_name])