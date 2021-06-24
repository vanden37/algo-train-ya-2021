num_list = list(map(int, input().split()))

c=0
for i in range(1,len(num_list)-1):
    if num_list[i] > num_list[i-1] and num_list[i] > num_list[i+1]:
        c += 1

print(c)