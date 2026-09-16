def count_bits(n):
    string_bits = str(bin(n).replace("0b",""))
    return string_bits.count("1")
print(count_bits(1234))