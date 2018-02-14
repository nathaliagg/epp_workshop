#!/usr/bin/env python

############# 
# written by N.Graf-Grachet
# goal: parse cazome to retrieve filtered output
# python ophio_cazome_getting_stats.py <cazy.txt> > <output.txt>
# status: finished!
#############

import sys
import re

# Open file
cazyme_output = open(sys.argv[1], 'r')

# Part1 - Parse hmmer_cazy output & add to annotation dictionary:
dict_cazymes = {}

for line in cazyme_output:
    if line.startswith('#'):
        continue
    else:
        column = line.rstrip().split()
        evalue = float(column[6])
        if evalue < 1e-5:
            gene_id = column[3]
            match = re.match(r"(.+).hmm", column[0])
            cazy_family = match.group(1)
            if cazy_family not in dict_cazymes:
                dict_cazymes[gene_id]=cazy_family
        else:
            continue

# Print output: cazymes filtered output
for gene_id in dict_cazymes:
    header = gene_id
    cazy = dict_cazymes[gene_id]
    print(header,cazy)


