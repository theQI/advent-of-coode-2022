# open file
with open("day2.txt") as file:
    rounds = [line.rstrip() for line in file]

points_dict = {
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

points_keeper = 0

for round in rounds:
    point = points_dict.get(round)
    points_keeper = points_keeper + point


print(f"My points: {points_keeper}")
