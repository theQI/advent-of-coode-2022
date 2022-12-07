with open("day5.txt") as file:
    lines = [line.rstrip() for line in file]
    guide = lines[10:]


stacks = {
    "1": ["N", "C", "R", "T", "M", "Z", "P"],
    "2": ["D", "N", "T", "S", "B", "Z"],
    "3": ["M", "H", "Q", "R", "F", "C", "T", "G"],
    "4": ["G", "R", "Z"],
    "5": ["Z", "N", "R", "H"],
    "6": ["F", "H", "S", "W", "P", "Z", "L", "D"],
    "7": ["W", "D", "Z", "R", "C", "G", "M"],
    "8": ["S", "J", "F", "L", "H", "W", "Z", "Q"],
    "9": ["S", "Q", "P", "W", "N"],
}


for a in guide:
    splits = a.split(" ")
    crates_count = int(splits[1])
    from_stack = splits[3]
    to_stack = splits[5]
    moving_crates = stacks[from_stack][-crates_count:]
    # reverse the moving crates for part 1 answer
    # moving_crates.reverse()
    del stacks[from_stack][-crates_count:]
    stacks[to_stack] = stacks[to_stack] + moving_crates

end_of_stack = []

for stack in stacks.keys():
    end_of_stack.append(stacks[stack][-1])

print(f"""Part 2 answer: {"".join(end_of_stack)}""")
