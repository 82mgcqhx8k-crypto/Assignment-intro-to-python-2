# Basic Python Commands
# Yash
# 09/25/26

# 1.

# Read sequnce from file
with open('chr1_GL383518v1_alt.fa', 'r') as f:
    read_lines = f.readlines()

# Remove header
header_line = [line.strip() for line in read_lines if not line.startswith('>')]

# Combine all sequence lines into singular string
sequence = ''.join(header_line)

# Print 10th letter
print('10th letter:', sequence[9])

# Print 758th letter
print('758th letter:', sequence[757])

# Line breaker to separate my results
print('\n')

# 2.

# Define Watson-Crick base pair rules
comp_pairs = str.maketrans('ACGT', 'TGCA')

reverse_complement = sequence.translate(comp_pairs)[::-1]

# Print 79th letter
print('79th letter:', reverse_complement[78])

# Print letters from 500 to 800
print('Letters 500 - 800:', reverse_complement[499:800])

# Line breaker
print('\n')

# 3.

# Make an empty dictionary
my_dict = {}

for start in range(0, len(sequence), 1000):
    base_segment = sequence[start:start+1000]

    my_dict[start] = {
        'A': base_segment.count('A'),
        'C': base_segment.count('C'),
        'G': base_segment.count('G'),
        'T': base_segment.count('T'),
    }

# Print number of times each letter appears
print('Segement counts at Position 5000\n',my_dict.get(5000))

# Line breaker
print('\n')

# 4.

# List of nuclotide counts
first_kilo = [
    my_dict[0]['A'],
    my_dict[0]['C'],
    my_dict[0]['G'],
    my_dict[0]['T'],
]

# Print first 1,000 bases
print('First kilobase:', first_kilo)

# Collect lists into one list

all_kilobase_count = []

for start in my_dict:
    count = [
        my_dict[start]['A'],
        my_dict[start]['C'],
        my_dict[start]['G'],
        my_dict[start]['T'],
    ]
    all_kilobase_count.append(count)

# Compute and print sum of each list
kilo_sum = [sum(count) for count in all_kilobase_count]
print('Sum of each kilobase list:', kilo_sum)

for start, total in zip(my_dict, kilo_sum):
    expect_sum = min(1000, len(sequence) - start)

    # print the difference between expected and observed results
    if total != expect_sum:
        print(
            f'Segment starting at {start}: sum is {total}, expected {expect_sum}'
        )

# Answer to e1 and e2
# e1: the expected sum for each list is 1,000
# e2: there were many lists there didn't equal the expected value of sum