num_list = list(map(int, input().split()))

sort_right = sorted(num_list)
sort_left = sorted(num_list, reverse = True)

product_right = sort_right[0]*sort_right[1]*sort_right[2]

product_left = sort_left[0]*sort_left[1]*sort_left[2]

prod_mix = sort_right[0]*sort_right[1]*sort_left[0]

if max(product_right, product_left, prod_mix) == product_right:
    print(f'{sort_right[0]} {sort_right[1]} {sort_right[2]}')
elif max(product_right, product_left, prod_mix) == product_left:
    print(f'{sort_left[2]} {sort_left[1]} {sort_left[0]}')
elif max(product_right, product_left, prod_mix) == prod_mix:
    print(f'{sort_right[0]} {sort_right[1]} {sort_left[0]}')