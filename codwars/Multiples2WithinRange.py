def multiples(a: int, b: int, limit: int) -> list[int]:
    multiples_list = []
    for i in range(1,limit+1):
        if i % a == 0 or i % b == 0:
            multiples_list.append(i)
    return multiples_list