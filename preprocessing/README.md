# Preprocessing

## 1. Download all bacterial protein sequences from UniProt

1. Go to the UniProt website (www.uniprot.org).
2. In the search box, enter "taxonomy\:bacteria" to filter for all bacterial proteins.
3. Click on the "Download" button at the top of the search results.
4. Unzip the GZ file downloaded

## 2. Sort the bacterial protein by species

1. Create `output_species_files` directory within preprocessing
2. Run `pip install biopython`
3. Run `python sort_species.py`

## 3. Generate the input_file.txt

1. Run `python generate_input_file`.py

## 4. Generate Config File

1. Run `python generate_config.py`
