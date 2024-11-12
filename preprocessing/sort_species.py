from Bio import SeqIO
from collections import defaultdict

# Read the input FASTA file
input_file = "uniprotkb_taxonomy_bacteria_2024_11_12.fasta"
output_dir = "output_species_files/"

# Create a dictionary to store sequences for each species
species_sequences = defaultdict(list)

# Parse the input FASTA file
for record in SeqIO.parse(input_file, "fasta"):
    # Extract species name from the description
    description = record.description
    species = description.split("OS=")[1].split("OX=")[0].strip()
    
    # Add the sequence to the corresponding species list
    species_sequences[species].append(record)

# Write sequences for each species to separate FASTA files
for species, sequences in species_sequences.items():
    # Create a valid filename by replacing spaces with underscores
    filename = species.replace(" ", "_") + ".fasta"
    output_file = output_dir + filename
    
    # Write sequences to the output file
    SeqIO.write(sequences, output_file, "fasta")
    
    print(f"Created file: {output_file}")