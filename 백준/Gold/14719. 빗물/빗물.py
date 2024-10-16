h, w = map(int, input().split())
tall = 0
tall_idx = 0
heights = [0] * w
for idx, value in enumerate(list(map(int, input().split()))):
    heights[idx] = value
    if tall < value:
        tall = value
        tall_idx = idx

prefix = [item for item in heights]
for i in range(0, tall_idx):
    prefix[i + 1] = max(prefix[i], prefix[i + 1])

for i in range(w - 1, tall_idx, -1):
    prefix[i - 1] = max(prefix[i], prefix[i - 1])

print(sum(prefix) - sum(heights))
