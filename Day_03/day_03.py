from collections import namedtuple
from itertools import product


Claim = namedtuple('Claim', 'id coord_x coord_y size_x size_y')


def get_raw_data(line):
    id, _, start_coord, size = line.split(" ")
    coord_x, coord_y = tuple(map(lambda x: int(x), start_coord[:-1].split(",")))
    size_x,  size_y = tuple(map(lambda x: int(x), size.split("x")))
    return Claim(id=id, coord_x=coord_x, coord_y=coord_y, size_x=size_x, size_y=size_y)


def get_claim_set(claim):
    return set(
        product(
            range(claim.coord_x, claim.coord_x + claim.size_x),
            range(claim.coord_y, claim.coord_y + claim.size_y)
        )
    )


with open("input", "r") as f:
    lines = f.read().splitlines()
claims = tuple(map(get_raw_data, lines))
once = set()
twice = set()
for i, claim in enumerate(claims):
    new_set = get_claim_set(claim)
    intersect = once.intersection(new_set)
    once = once.union(new_set)
    twice.update(intersect)
print(len(twice))


###

for claim in claims:
    new_set = get_claim_set(claim)
    if not twice.intersection(new_set):
        print(claim.id)

