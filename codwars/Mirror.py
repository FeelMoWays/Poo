def mirror(data: list) -> list:
    sorted_list = sorted(data)
    return sorted_list + sorted_list[-2::-1]
print(mirror([1,3,2]))