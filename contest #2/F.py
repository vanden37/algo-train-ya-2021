c = 0

n = int(input())
seq = list(map(int, input().split()))
init_seq = seq
while True:

    mid = (n-1)//2
    start = 0
    last = n-1
    flag = 0

    while(start <= mid):

        if (seq[start]== seq[last]):
              
            start += 1
            last -= 1
              
        else:
            flag = 1
            c += 1
            break;

    if flag == 0:
        print(c)
        if c > 0:
            print(*init_seq[c-1::-1])
        break

    else:
        seq = init_seq + init_seq[c-1::-1]
        n = len(seq)