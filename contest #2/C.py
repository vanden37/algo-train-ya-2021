n = int(input())
num_list = list(map(int, input().split()))
x = int(input())

dif = []                
for el in num_list:
   dif.append(x-el)
   
dif = list(map(abs, dif))
                
print(num_list[dif.index(min(dif))])  