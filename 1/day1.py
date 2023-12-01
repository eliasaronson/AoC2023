import regex as re

file = open('input.txt')
lines = file.readlines()
part = 2

rep = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
match_exp = "(\d|one|two|three|four|five|six|seven|eight|nine|ten)" if part == 2 else "\d"

def trans(match):
    if match in rep:
        return rep[match]
    return match

total = 0
for line in lines:
    matches = re.findall(match_exp, line, overlapped=True)
    matches = [i for i in matches if i]
    matches = list(map(trans, matches))
    total += int(matches[0] + matches[-1])

file.close()

print(f"{total=}")
