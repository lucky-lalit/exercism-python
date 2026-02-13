def to_rna(dna_strand):
    str = ''
    if len(dna_strand) <= 1:
        if 'G' in dna_strand:
            return dna_strand.replace('G','C')
        elif 'C' in dna_strand:
            return dna_strand.replace('C','G')
        elif 'T' in dna_strand:
            return dna_strand.replace('T','A')
        elif 'A' in dna_strand:
            return dna_strand.replace('A','U')
        else:
            return dna_strand
    else:
        dna_strand = dna_strand.replace('G','M')
        dna_strand = dna_strand.replace('C','G')
        dna_strand = dna_strand.replace('M','C') 
        dna_strand = dna_strand.replace('T','N')
        dna_strand = dna_strand.replace('A','U')
        dna_strand = dna_strand.replace('N','A')
        return dna_strand