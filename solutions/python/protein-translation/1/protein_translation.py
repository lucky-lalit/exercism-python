def proteins(strand):
    CODONS = {
        'AUG':'Methionine',
        'UUU':'Phenylalanine',
        'UUC':'Phenylalanine',
        'UUA':'Leucine',
        'UUG':'Leucine',
        'UCU':'Serine',
        'UCC':'Serine',
        'UCA':'Serine',
        'UCG':'Serine',
        'UAU':'Tyrosine',
        'UAC':'Tyrosine',
        'UGU':'Cysteine',
        'UGC':'Cysteine',
        'UGG':'Tryptophan',
        'UAA':'STOP',
        'UAG':'STOP',
        'UGA':'STOP'
    }
    lst = []
    while len(strand) >= 3:
        RNA_str = strand[:3]
        if CODONS[RNA_str] != 'STOP':
            lst.append(CODONS[RNA_str])
        else:
            return lst
        strand = strand[3:]
    return lst
    
    
        
    