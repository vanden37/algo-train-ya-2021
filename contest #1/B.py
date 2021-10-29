a = int(input())
b = int(input())
c = int(input())

if a == 0 or b == 0 or c == 0:
    print("NO")
else:

    if ((a + b) <= c) or ((a + c) <= b) or ((b + c) <= a):
        print("NO")
    else:
        print("YES")