S = "qA2"
if not S.isalnum():
    print("False")
else: 
    for i in S:
        if i.isalnum():
            print("True")
            break

if not S.isalpha():
    print("False")
else:
    for i in S:
        if i.isalpha():
            print("True")
            break

if not S.isdigit():
    print("False")
else:
    for i in S:
        if i.isdigit():
            print("True")
            break
    
if not S.islower():
    print("False")
else:
    for i in S:
        if i.islower():
            print("True")
            break
    
if not S.isupper():
    print("False")
else:
    for i in S:
        if i.isupper():
            print("True")
            break
