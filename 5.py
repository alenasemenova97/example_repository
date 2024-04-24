a = [int(x) for x in open('03.txt').readlines()]

m = len([x for x in a if abs(x) % 5 == 0])

tmp = []
for i in range(len(a) - 1):
    s = (a[i] < 0) + (a[i + 1] < 0)
    if s == 1 and a[i] + a[i + 1] < m:
        tmp.append(a[i] + a[i + 1])
print(len(tmp), max(tmp))