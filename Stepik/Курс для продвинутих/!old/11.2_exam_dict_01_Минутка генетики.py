dna_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
dna = input('Введите ДНК: ')
rna = ''
for i in dna:
    rna += dna_rna[i]
print(rna)