num_list = list(map(int, input().split()))

sort_right = sorted(num_list)
sort_left = sorted(num_list, reverse = True)

product_right = sort_right[0]*sort_right[1]

product_left = sort_left[0]*sort_left[1]

print(f'{sort_right[0]} {sort_right[1]}' if max(product_right,product_left) == product_right else f'{sort_left[1]} {sort_left[0]}')