import sys
from functools import reduce

lines = []
with open("input", "r") as f:
    for l in f:
        lines.append(l[:-1])

incrementations = list(map(lambda x: int(x), lines))
end_frequency = reduce(lambda x, y: x + y, incrementations)
print(end_frequency)

###

consecutive_freq = [0]
for i in incrementations:
    consecutive_freq.append(consecutive_freq[-1] + i)

for idx, freq in enumerate(consecutive_freq[:-1]):
    val = freq
    while any(f >= val for f in consecutive_freq[:-1]):
        if any(f == val and idx != idx2 for idx2, f in enumerate(consecutive_freq[:-1])):
            print(val)
            sys.exit(0)
        val += end_frequency
