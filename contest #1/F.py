dims = list(map(int, input().split()))

max1 = max(dims[:2])
min2 = min(dims[2:])
           
min1 = min(dims[:2])
max2 = max(dims[2:])

sq1 = (min1 + min2) * max(max1, max2)
sq2 = (max1 + max2) * max(min1, min2)

sq3 = (min1 + max2) * max(max1, min2)
sq4 = (min2 + max1) * max(min1, max2)

if sq1 == min(sq1, sq2, sq3, sq4):
    print(f'{(min1 + min2)} {max(max1, max2)}')
elif sq2 == min(sq1, sq2, sq3, sq4):
    print(f'{(max1 + max2)} {max(min1, min2)}')
elif sq3 == min(sq1, sq2, sq3, sq4):
    print(f'{(min1 + max2)} {max(max1, min2)}')
elif sq4 == min(sq1, sq2, sq3, sq4):
    print(f'{(min2 + max1)} {max(min1, max2)}')