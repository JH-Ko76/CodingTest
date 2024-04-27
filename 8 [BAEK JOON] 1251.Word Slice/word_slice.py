import sys
n = sys.stdin.readline().strip()
words = []

for i in range(1, len(n)):
    for j in range(i + 1, len(n)):
        word1 = n[:i][::-1]
        word2 = n[i:j][::-1]
        word3 = n[j:][::-1]
        words.append(word1 + word2 + word3)

print(sorted(words)[0])