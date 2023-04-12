dic1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1}
cnt = 0
for v in dic1.values():
    if v == 1:
        cnt = cnt+1

print(cnt)
