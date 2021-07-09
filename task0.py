import random

n = []
maxn = -100
maxnid = -1

for i in range(30):
    n.append(random.randint(-100,100))
    print(n[i])

    if maxn < n[i]:
        maxn = n[i]
        maxnid = i

print("\nMax number:", maxn, "\nMax number id:", maxnid, "\n\n")

for i in range(29):
    if n[i] < 0 and n[i+1] < 0:
        print(n[i], n[i+1], "\n")
