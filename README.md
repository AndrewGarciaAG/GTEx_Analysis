# GTEx_Analysis
This script reads a list of genomic coordinates and associated variant information from a CSV file and fetches the corresponding records from a VCF file. It prints detailed information about each variant, including the genotype of each sample.

# VCF Variant Fetcher
This script reads a list of genomic coordinates and associated variant information from a CSV file and fetches the corresponding records from a VCF file. It prints detailed information about each variant, including the genotype of each sample.

## Requirements
- Python 3.6+
- `pysam` library

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/vcf-variant-fetcher.git
    cd vcf-variant-fetcher
    ```
2. Install the required Python package:
    ```bash
    pip install pysam
    ```

## Usage
1. **Prepare your coordinate file:** Create a CSV file with the following columns: `chromosome`, `position`, `ref_allele`, `alt_allele`. Each row should represent one variant coordinate. For example:

    ```csv
    chromosome,position,ref_allele,alt_allele
    chr1,13526,,
    chrX,153059915,C,T
    chr9,91933357,C,T
    ```

2. **Set file paths:** Replace the example paths in the `main` function of the script with the paths to your actual VCF file and coordinates CSV file.

3. **Run the script:**
    ```bash
    python vcf_variant_fetcher.py
    ```

## Example

### Coordinates CSV File (`coordinates.csv`)

```csv
chromosome,position,ref_allele,alt_allele
chr1,13526,,
chrX,153059915,C,T
chr9,91933357,C,T

