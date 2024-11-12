import os

# Directory containing the species FASTA files
output_dir = "output_species_files/"

# Full path to the output directory
full_path = os.path.abspath(output_dir)

# Output file name
input_file = "input_file.txt"

# Get list of FASTA files
fasta_files = [f for f in os.listdir(full_path) if f.endswith('.fasta')]

# Sort files by size (ascending)
fasta_files.sort(key=lambda f: os.path.getsize(os.path.join(full_path, f)))

# Write to input file
with open(input_file, 'w') as f:
    f.write("# MetaProFi input file for bacterial species\n")
    for fasta_file in fasta_files:
        species_name = fasta_file.replace('.fasta', '')
        file_path = os.path.join(full_path, fasta_file)
        f.write(f"{species_name}: {file_path}\n")

print(f"Input file '{input_file}' has been created.")