from itertools import combinations

lines = []
with open("input", "r") as f:
    lines = [line[:-1] for line in f]

twos = 0
threes = 0
for line in lines:
    a = {}
    for c in line:
        a[c] = a[c] + 1 if c in a else 1
    if 2 in a.values():
        twos += 1
    if 3 in a.values():
        threes += 1
print(twos * threes)


###

def resemble(w1, w2):
    count = 0
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            count += 1
    return count / len(w1)


w1, w2, _ = sorted([(a, b, resemble(a, b)) for a, b in combinations(lines, 2)], key=lambda x: x[2])[-1]

final = []
for i in range(len(w1)):
    if w1[i] == w2[i]:
        final.append(w1[i])
print("".join(final))