with open("day3.txt") as file:
    lines = [line.rstrip() for line in file]

priority_dict = {}

for idx, i in enumerate(range(ord("a"), ord("z") + 1)):
    priority_dict[chr(i)] = idx + 1

for idx, i in enumerate(range(ord("A"), ord("Z") + 1)):
    priority_dict[chr(i)] = idx + 1 + 26

priority_sum = 0
for item in lines:
    first, second = item[: len(item) // 2], item[len(item) // 2 :]
    common = set(first) & set(second)
    priority_sum = priority_sum + priority_dict[list(common)[0]]

print(f"Sum of common items priority: {priority_sum}")
