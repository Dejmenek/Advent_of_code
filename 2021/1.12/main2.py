raw_ocean_depths = open('input.txt','r')
ocean_depths = raw_ocean_depths.read()
ocean_depths = ocean_depths.splitlines()

data = [int(n) for n in ocean_depths]

sum = 0

for i, distance in enumerate(data[3:],3):
    previous_dephts_sum = data[i-3:i]
    current_dephts_sum = data[i-2:i+1]
    if previous_dephts_sum < current_dephts_sum:
        sum +=1

print(sum)
