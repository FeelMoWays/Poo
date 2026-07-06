def to_rna(dna_strand):
    bict = {
        "G":"C",
        "C":"G",
        "T":"A",
        "A":"U",
    }
    sto = ""
    for i in dna_strand:
        sto += bict[i]
    return sto
print(to_rna("ACGTGGTCTTAA"))