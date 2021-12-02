raw_ocean_depths = open('input.txt','r')
ocean_depths = raw_ocean_depths.read()
ocean_depths = ocean_depths.splitlines()

ocean_dephts_list = [int(n) for n in ocean_depths]

sum = 0

for i in range(1,len(ocean_dephts_list)):
    previous_depth = ocean_dephts_list[i-1]
    current_depth = ocean_dephts_list[i]
    if previous_depth < current_depth:
        sum += 1

print(sum)