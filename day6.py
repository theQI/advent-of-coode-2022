with open("day6.txt", "r", encoding="utf-8") as input:
    datastream = input.read().strip()

print(datastream)
print(len(datastream))

for i in range(len(datastream)):
    start_of_packet = datastream[i : i + 4]
    if len(set(start_of_packet)) == 4:
        print(f"Part 1 answer: {i+4}")
        break


for i in range(len(datastream)):
    start_of_message = datastream[i : i + 14]
    if len(set(start_of_message)) == 14:
        print(f"Part 2 answer: {i+14}")
        break
