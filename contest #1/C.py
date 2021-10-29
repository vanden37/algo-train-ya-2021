new_num = str(input())
f_num = str(input())
s_num = str(input())
t_num = str(input())

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

all_nums = [new_num, f_num, s_num, t_num]
nums = []
for num in all_nums:
    nums.append([n for n in num if n in num_list])

for ind, val in enumerate(nums):
    if len(val) == 7:
       nums[ind] = ['4','9','5'] + val

list_nums = nums[1:]

for num in list_nums:
    if num[-10:] == nums[0][-10:]:
        print("YES")
    else:
        print("NO")