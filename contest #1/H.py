t_between_a = int(input())
t_between_b = int(input())
n_stops_a = int(input())
n_stops_b = int(input())

t_stop = 1

min_a  = t_stop * n_stops_a + (n_stops_a - 1) * t_between_a
max_a = t_stop * n_stops_a + (n_stops_a + 1) * t_between_a

min_b  = t_stop * n_stops_b + (n_stops_b - 1) * t_between_b
max_b = t_stop * n_stops_b + (n_stops_b + 1) * t_between_b

a = max(min_a, min_b)
b = min(max_a, max_b)

if max_a < min_b or max_b < min_a:
    print(-1)
else:
    print(a, b)