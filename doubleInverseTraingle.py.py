print("input:")
x = int(input())
for i in range(0, x):
    list1 = []
    for j in range(0, x):
        if i >= x - j:
            list1.append(" ")
        else:
            list1.append(x - j)

    for k in range(x, 1, -1):
        if i >= x - k + 2:
            list1.append(" ")
        else:
            list1.append(x - k + 2)

    print(*list1)
