raw_ocean_depths = open('2021//2.12//day2.txt','r')
data = raw_ocean_depths.readlines()


def part_one():
    horizontal,depth = 0, 0
    for command in data:
        direction, amount = command.split()
        if direction == "forward":
            horizontal += int(amount)
        elif direction == "down":
            depth += int(amount)
        elif direction == "up":
            depth -= int(amount)
    return horizontal*depth

def part_two():
    horizontal, depth, aim = 0, 0, 0
    for command in data:
        direction, amount = command.split()
        if direction == "forward":
            horizontal += int(amount)
            depth += int(amount) * aim
        elif direction == "down":
            aim += int(amount)
        elif direction == "up":
            aim -= int(amount)
    return horizontal*depth

print(part_one())
print(part_two())