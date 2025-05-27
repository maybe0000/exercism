def proteins(strand: str):
    codons_proteins = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
    }
    stop_codons = {"UAA", "UAG", "UGA"}
    protein_translation = []
    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]
        if codon in stop_codons:
            if i == 0:
                return []
            else:
                break
        protein_translation.append(codons_proteins[codon])
    return protein_translation
