import os

genomes_directory_names = '/scratch/mbr5797/genomes_extracted_from_kegg'

if __name__ == '__main__':
    directories = [name for name in os.listdir(genomes_directory_names) if os.path.isdir(os.path.join(genomes_directory_names, name))]
    print(directories[:10])