t = int(input())
for _ in range(t):
    a = int(input());
    list =[]
    for _ in range(a):
        b = int(input())
        list.append(b)
        max_b = max(list)
        min_b = min(list)
        final = max_b - min_b;
        print(final)
