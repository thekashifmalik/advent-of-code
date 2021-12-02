with open('input') as f:
    INPUT = f.read().splitlines()

increased = 0
for idx, value in enumerate(INPUT):
    if idx == 0:
        continue
    if int(value) > int(INPUT[idx - 1]):
        increased += 1

print(increased)
