n = int(input())
alphabet = {}
words = []
max_len = 0
for _ in range(n):
    word = input()
    words.append(word)
    if len(word) > max_len:
        max_len = len(word)

for idx in range(n):
    if len(words[idx]) < max_len:
        words[idx] = words[idx].zfill(max_len)
    words[idx] = list(words[idx])

for char_idx in range(max_len):
    for word_idx in range(n):
            if words[word_idx][char_idx] == '0': continue
            if not words[word_idx][char_idx] in alphabet:
                 alphabet[words[word_idx][char_idx]] = 0
            alphabet[words[word_idx][char_idx]] += 10 ** (max_len - char_idx - 1)

data = []
for key in alphabet:
    data.append((alphabet[key], key))

data.sort(reverse=True)

for idx in range(len(data)):
    alphabet[data[idx][1]] = 9 - idx

for char_idx in range(max_len):
    for word_idx in range(n):
        if words[word_idx][char_idx] == '0': continue
        words[word_idx][char_idx] = str(alphabet[words[word_idx][char_idx]])

answer = 0
for char_list in words:
    answer += int("".join(char_list))

print(answer)