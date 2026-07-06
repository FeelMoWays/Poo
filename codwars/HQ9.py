def HQ9(code):
    if code == "H":
        return "Hello World!"
    elif code == "Q":
        return code
    elif code == "9":
        return "\n".join(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i-1} bottles of beer on the wall." for i in range(99, 0, -1))
    else:
        return None