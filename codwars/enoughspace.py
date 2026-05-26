def enough(cap, on, wait):
    u = on + wait
    if cap >= u:
        return 0
    return u - cap
