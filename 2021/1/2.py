with open('input') as f:
    INPUT = list(map(int, f.read().splitlines()))

increased = 0
for idx, value in enumerate(INPUT):
    if idx == 0:
        continue
    if idx + 2 >= len(INPUT):
        break
    previous = INPUT[idx - 1] + value + INPUT[idx + 1]
    current = value + INPUT[idx + 1] + INPUT[idx + 2]
    if current > previous:
        increased += 1

print(increased)
