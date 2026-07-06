def smallest_transform(num):
    digits = [int(d) for d in str(num)]
    min_num  = float("inf")
    for target in range(10):
        cost = sum(abs(d - target) for d in digits )
        min_cost = min(min_num,cost)
    return min_cost