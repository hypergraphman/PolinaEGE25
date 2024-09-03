print('a b c d')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = int((a <= b) and (b <= (not c)) and ((not c) <= d))
                if f == 1:
                    print(a, b, c, d)