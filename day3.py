with open("day3.txt") as file:
    lines = [line.rstrip() for line in file]

priority_dict = {}

for idx, i in enumerate(range(ord("a"), ord("z") + 1)):
    priority_dict[chr(i)] = idx + 1

for idx, i in enumerate(range(ord("A"), ord("Z") + 1)):
    priority_dict[chr(i)] = idx + 1 + 26

# Part 1
part1_priorities = 0
for item in lines:
    first, second = item[: len(item) // 2], item[len(item) // 2 :]
    common = set(first) & set(second)
    part1_priorities = part1_priorities + priority_dict[list(common)[0]]

print(f"Part 1 answer: {part1_priorities}")

# Part 2
part2_priorities = 0
group_items = []
for idx, item in enumerate(lines):
    group_items.append(item)
    if (idx + 1) % 3 == 0:
        common = set(group_items[0]) & set(group_items[1]) & set(group_items[2])
        part2_priorities = part2_priorities + priority_dict[list(common)[0]]
        group_items = []

print(f"Part 2 answer: {part2_priorities}")
