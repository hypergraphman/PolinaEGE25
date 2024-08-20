print('a b c f')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(not ((not a) <= (b <= (not c))))
            f2 = int(not a and b and c)
            print(a, b, c, f, f2)