"""Placeholdr for program documentaion"""
"""comments for the test"""

import sys

def read_fasta(filename):
    sequence = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            # Append to the last sequence
            sequence = sequence + line
    f.close()
    return sequence

print read_fasta(sys.argv[1])
