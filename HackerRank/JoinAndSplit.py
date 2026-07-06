

def split_and_join(line):
    u = line.split(" ")
    return "-".join(u)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)