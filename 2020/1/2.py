with open('input') as f:
    INPUT = f.read().splitlines()


for idx1, line1 in enumerate(INPUT):
    for idx2, line2 in enumerate(INPUT):
        for idx3, line3 in enumerate(INPUT):
            if idx1 == idx2 or idx1 == idx3 or idx2 == idx3:
                continue
            total = int(line1) + int(line2) + int(line3)
            if total == 2020:
                print(f'OK: {int(line1) * int(line2) * int(line3)}')
