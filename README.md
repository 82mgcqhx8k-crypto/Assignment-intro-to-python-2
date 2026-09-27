# Assignment-intro-to-python-2

# README.md

## DNA Kilobase Nucleotide Counts

### Identifying information
- **Programmer:** [Yash]
- **Language:** Python 
- **Date submitted:** [2026-27-09]

### Purpose
This script reads a DNA sequence from a FASTA file, counts A, C, G, and T in consecutive segments of up to 1,000 bases, and prints the counts and their sums. 

### Required files
- **`chr1_GL383518v1_alt.fa`** — input FASTA file containing the DNA sequence. Place it in the same folder as the script, or update the script with its correct path.

The program prints the A, C, G, and T counts for the first kilo base, the sums for all segments, and any segments whose sums differ from their expected lengths. A final segment shorter than 1,000 bases is expected if the sequence length is not divisible by 1,000. Ambiguous bases such as `N` are not included in the A,C,G,T counts. It also uses slicing and indexing to find nucleotide letter on specific number e.g. 10th letter = c
