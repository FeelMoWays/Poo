def alphabet_war(fight):
    right = {'m':4,'q':3,'d':2,'z':1}
    left = {'w':4,'p':3,'b':2,'s':1}
    count1 = 0
    count2 = 0
    for i in fight:
        if i in right.keys():
            count1 += right[i]
        elif i in left.keys():
            count2 += left[i]
        else:
            count1 += 0
            count2 += 0
    if count1 > count2:
        return ('Right side wins!')
    elif count2 > count1:
        return ('Left side wins!')
    else:
        return("Let's fight again!")


