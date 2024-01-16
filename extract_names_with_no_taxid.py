import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('list_of_taxids', sep='\t', header=None)
    df.columns = ['scientific_name', 'taxid']
    for scientific_name, taxid in list( zip(df['scientific_name'].tolist(), df['taxid'].tolist()) ):
        if str(taxid) == 'nan':
            print(scientific_name)