with open('input') as f:
    INPUT = f.read().splitlines()


for idx1, line1 in enumerate(INPUT):
    for idx2, line2 in enumerate(INPUT):
        if idx1 == idx2:
            continue
        total = int(line1) + int(line2)
        if total == 2020:
            print(f'OK: {int(line1) * int(line2)}')
