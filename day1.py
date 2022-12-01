# open file
with open("day1.txt") as file:
    lines = [line.rstrip() for line in file]

# initialize
calories_sum = 0
calories_list = []
for x in lines:
    if x != "":
        calories_sum = calories_sum + int(x)
    else:
        calories_list.append(calories_sum)
        calories_sum = 0

elfs = len(calories_list)

calories_list = sorted(calories_list)

print(f"Top Carrier: {calories_list[elfs-1]}")
print(
    f"Sum of Top 3: {calories_list[elfs-1] + calories_list[elfs-2] + calories_list[elfs-3]}"
)
