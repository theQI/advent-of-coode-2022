with open("day4.txt") as file:
    pairs = [line.rstrip() for line in file]

fully_contained_count = 0
for pair in pairs:
    elf1, elf2 = pair.split(",")
    elf1_lower, elf1_upper = elf1.split("-")
    elf2_lower, elf2_upper = elf2.split("-")
    print(elf1_lower, elf1_upper, elf2_lower, elf2_upper)
    if (int(elf1_lower) <= int(elf2_lower)) & (int(elf1_upper) >= int(elf2_upper)):
        print("Case 1")
        fully_contained_count = fully_contained_count + 1
    elif (int(elf1_lower) >= int(elf2_lower)) & (int(elf1_upper) <= int(elf2_upper)):
        print("Case 2")
        fully_contained_count = fully_contained_count + 1

print(f"Part 1 answer: {fully_contained_count}")
