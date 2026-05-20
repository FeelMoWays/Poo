def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach !"
    elif type(x) == float or type(x) == int:
        return "Who ate the last cookie? It was Monica !"
    else:
        return "Who ate the last cookie? It was the dog !"
