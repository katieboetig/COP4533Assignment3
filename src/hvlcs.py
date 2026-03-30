import sys

def main():
    lines = sys.stdin.read().splitlines()
    line_index = 0

    # Number of character values
    num_chars = int(lines[line_index])
    line_index += 1

    # Map character to its value
    char_values = {}
    for _ in range(num_chars):
        char, value = lines[line_index].split()
        char_values[char] = int(value)
        line_index += 1

    # Read the two sequences
    seq1 = lines[line_index].strip()
    line_index += 1
    seq2 = lines[line_index].strip()

    len1, len2 = len(seq1), len(seq2)

    # Build DP table for max weighted common subsequence
    dp_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i-1] == seq2[j-1]:
                dp_table[i][j] = max(
                    dp_table[i-1][j-1] + char_values.get(seq1[i-1], 0),
                    dp_table[i-1][j],
                    dp_table[i][j-1]
                )
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

    # Reconstruct the weighted common subsequence
    common_seq = []
    i, j = len1, len2
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1] and dp_table[i][j] == dp_table[i-1][j-1] + char_values.get(seq1[i-1], 0):
            common_seq.append(seq1[i-1])
            i -= 1
            j -= 1
        elif dp_table[i-1][j] >= dp_table[i][j-1]:
            i -= 1
        else:
            j -= 1

    print(dp_table[len1][len2])
    print(''.join(reversed(common_seq)))

if __name__ == "__main__":
    main()