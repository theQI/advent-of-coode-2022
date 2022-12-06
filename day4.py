with open("day4.txt") as file:
    pairs = [line.rstrip() for line in file]

fully_contained = []
overlapped = []
for pair in pairs:
    elf1, elf2 = pair.split(",")
    elf1_lower, elf1_upper = elf1.split("-")
    elf2_lower, elf2_upper = elf2.split("-")
    print(elf1_lower, elf1_upper, elf2_lower, elf2_upper)
    x = set(range(int(elf1_lower), int(elf1_upper) + 1))
    y = set(range(int(elf2_lower), int(elf2_upper) + 1))
    intersect = x.intersection(y)
    overlapped.append(len(intersect) > 0)
    fully_contained.append((intersect == x) | (intersect == y))

print(f"Part 1 answer {sum(fully_contained)}")
print(f"Part 2 answer {sum(overlapped)}")
