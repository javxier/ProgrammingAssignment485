# This project is made for terminal use with python
# You can proceed with the directions for python
#
# Open VSCODE, any IDE, with terminal open
# or simply on the terminal with python installed on the machine
# run as python file
# you will be prompted for input. Proceed
# It will give you a matrix, edit distance, and alignment

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i

    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp

def print_alignment(matrix, word1, word2):
    i, j = len(word1), len(word2)
    alignment_word1 = []
    alignment_word2 = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            alignment_word1.append(word1[i-1])
            alignment_word2.append(word2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or matrix[i][j] == matrix[i-1][j] + 1):
            alignment_word1.append(word1[i-1])
            alignment_word2.append("_")
            i -= 1
        else:
            alignment_word1.append("_")
            alignment_word2.append(word2[j-1])
            j -= 1

    return ''.join(alignment_word1[::-1]), ''.join(alignment_word2[::-1])

if __name__ == "__main__":
    print()
    print("Welcome to Edit Distance Demonstration.*")
    print("_______________________________________________")
    print("Please input two words for the edit distance:\n")
    word1 = input("The first word: ")
    word2 = input("The second word: ")
    print("_______________________________________________")

    matrix = edit_distance(word1, word2)
    edit_distance_value = matrix[len(word1)][len(word2)]

    print(f"\nThe matrix:")
    for row in matrix:
        print(' '.join(map(str, row)))

    print(f"\nThe edit distance is: {edit_distance_value}")
    alignment_word1, alignment_word2 = print_alignment(matrix, word1, word2)
    print(f"\nAlignment is:")
    print(alignment_word1)
    print(alignment_word2)
    print()
