import os
import yaml
from math import ceil, log

def calculate_bloom_filter_size(n, p):
    return ceil((n * log(p)) / log(1 / pow(2, log(2))))

def calculate_hash_functions(m, n):
    return round((m / n) * log(2))

def estimate_kmers(fasta_dir, k):
    total_kmers = 0
    for fasta_file in os.listdir(fasta_dir):
        if fasta_file.endswith('.fasta'):
            with open(os.path.join(fasta_dir, fasta_file), 'r') as f:
                sequence = ""
                for line in f:
                    if not line.startswith('>'):
                        sequence += line.strip()
                total_kmers += max(0, len(sequence) - k + 1)
    return total_kmers

# Directory containing the species FASTA files
fasta_dir = "output_species_files/"

# Parameters
k = 11  # K-mer size
p = 0.01  # Probability of false positives

# Estimate the maximum number of k-mers in the dataset
n = estimate_kmers(fasta_dir, k)

# Calculate Bloom filter size and number of hash functions
m = calculate_bloom_filter_size(n, p)
h = calculate_hash_functions(m, n)

# Configuration parameters
config = {
    'h': h,
    'k': k,
    'm': m,
    'nproc': 1,
    'max_memory': '60GiB',
    'sequence_type': 'aminoacid',
    'output_directory': 'output_dir',
    'matrix_store_name': 'metaprofi_bfmatrix',
    'index_store_name': 'metaprofi_index'
}

# Write to YAML file
with open('config.yml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

print("\nConfiguration file 'config.yml' has been created.")
print(f"Estimated maximum number of k-mers: {n}")
print(f"Calculated Bloom filter size (m): {m}")
print(f"Calculated number of hash functions (h): {h}")