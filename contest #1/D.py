a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')  
else:
    if a == 0 and (c ** 2 == b):
        print('MANY SOLUTIONS')
    elif a == 0 and (c ** 2 != b):
        print('NO SOLUTION')
    else:
        ans = (c ** 2 - b) / a
        if ans.is_integer() == True:
            print(int(ans))

        else:
            print('NO SOLUTION')