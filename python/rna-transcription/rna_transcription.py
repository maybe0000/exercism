def to_rna(dna_strand):
    rna_dict = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    rna_strand = ''
    for char in dna_strand:
        rna_strand += rna_dict[char]
    return rna_strand
