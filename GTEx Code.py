import pysam
import csv

def read_coordinates_from_file(file_path):
    """
    Reads coordinates and variant information from a CSV file.
    The CSV file should have columns: chromosome, position, ref_allele, alt_allele.
    """
    coordinates = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4:
                coordinates.append((row[0], int(row[1]), row[2], row[3]))
    return coordinates

def print_variant_info(record, chromosome, position, ref, alt):
    """
    Prints detailed variant information for the given record.
    """
    variant_info = {
        'chromosome': chromosome,
        'position': position,
        'ref_allele': ref,
        'alt_allele': alt,
        'samples': []
    }
    for sample in vcf.header.samples:
        genotype = record.samples[sample]['GT']
        variant_info['samples'].append((sample, genotype))
    print(f"Found variant at {chromosome}:{position} {ref}->{alt}: {variant_info}")

def fetch_records(vcf, chromosome, position, ref, alt):
    """
    Fetches records from the VCF file for the specified chromosome and position,
    and prints variant information if the record matches the specified ref and alt alleles.
    """
    found = False
    try:
        records = list(vcf.fetch(chromosome, start=position-1, end=position))
    except ValueError as e:
        print(f"Error fetching records for {chromosome}:{position}. Error: {e}")
        return

    for record in records:
        if record.pos == position:
            if ref and alt:
                # Case for specific ref and alt alleles
                if record.ref == ref and any(a == alt for a in record.alts):
                    found = True
                    print_variant_info(record, chromosome, position, ref, alt)
            elif not ref and not alt:
                # Case for positions without ref or alt specified
                found = True
                print_variant_info(record, chromosome, position, ref, alt)
            else:
                # Handle cases where only ref or only alt is specified
                if ref and record.ref == ref:
                    found = True
                    print_variant_info(record, chromosome, position, ref, alt)
                elif alt and any(a == alt for a in record.alts):
                    found = True
                    print_variant_info(record, chromosome, position, ref, alt)

    if not found:
        print(f"No variant found at {chromosome}:{position} {ref}->{alt} that matches criteria.")

def main(vcf_file_path, coordinates_file_path):
    """
    Main function to open the VCF file, read coordinates, and fetch records.
    """
    # Open the VCF file
    vcf = pysam.VariantFile(vcf_file_path)

    # Read coordinates from the file
    coordinates = read_coordinates_from_file(coordinates_file_path)

    # Process each coordinate
    for coord in coordinates:
        chromosome, position, ref_allele, alt_allele = coord
        fetch_records(vcf, chromosome, position, ref_allele, alt_allele)

    # Close the VCF file
    vcf.close()

if __name__ == "__main__":
    # Example usage
    vcf_file_path = '/path/to/your/vcf_file.vcf.gz'
    coordinates_file_path = '/path/to/your/coordinates.csv'
    main(vcf_file_path, coordinates_file_path)
