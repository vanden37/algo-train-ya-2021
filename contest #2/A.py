test_list = list(map(int, input().split()))

c = 1
if len(test_list) < 1:
    print("NO")
else:
    for i in range(len(test_list)-1):
        if test_list[i] >= test_list[i+1]:
           print("NO")
           break
        else:
            c += 1
            continue
if c == len(test_list):
    print("YES")