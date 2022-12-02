with open("day2.txt") as file:
    rounds = [line.rstrip() for line in file]

part1_dict = {
    "A Y": 8,
    "A X": 4,
    "A Z": 3,
    "B Y": 5,
    "B X": 1,
    "B Z": 9,
    "C Y": 2,
    "C X": 7,
    "C Z": 6,
}

part2_dict = {
    "A X": 3,
    "B X": 1,
    "C X": 2,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "A Z": 8,
    "B Z": 9,
    "C Z": 7,
}

part1_points = 0
part2_points = 0

for round in rounds:
    part1_score = part1_dict.get(round)
    part1_points = part1_points + part1_score
    part2_score = part2_dict.get(round)
    part2_points = part2_points + part2_score

print(f"Part 1 score: {part1_points}")
print(f"Part 2 score: {part2_points}")
