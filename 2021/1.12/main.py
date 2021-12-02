raw_ocean_depths = open('2021//1.12//day1.txt','r')
ocean_depths = raw_ocean_depths.read()
ocean_depths = ocean_depths.splitlines()

data = [int(n) for n in ocean_depths]

sum = 0

for i in range(1,len(data)):
    previous_depth = data[i-1]
    current_depth = data[i]
    if previous_depth < current_depth:
        sum += 1

print(sum)