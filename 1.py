input = "3 4 4 3 2 5 1 3 3 9 3 3"

l1 = []
l2 = []

frequency = {}

for (x,y) in enumerate(input.split()):
  if x %2 == 0:
    l1.append(int(y)) # part1
  else:
    y=int(y)
    l2.append(y) # part1
    frequency[y] = frequency[y] + 1 if y in frequency else 1 # part2

# remove this for better complexity on part 2
l1 = sorted(l1)
l2 = sorted(l2)

total_diff = 0
similarity_sum = 0
for x, y in enumerate(l1):
    diff = l2[x] - y # part1
    total_diff += diff if diff >= 0 else diff * -1 # part1
    similarity_sum += y * frequency[y] if y in frequency else 0 # part2


print(total_diff)
print(similarity_sum)
