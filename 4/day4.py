lines = open("input.txt").readlines()

total = 0
for line in lines:
    card = line.split(": ")[1]
    numbers = card.split(" | ")
    winners = numbers[0].split()
    your = numbers[1].split()
    intersect = [x for x in your if x in winners]
    num_winners = len(intersect)
    if num_winners:
        total += 2**(len(intersect) - 1)

print(f"{total=}")
