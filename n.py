def f(n):
    if not n:
        return None
    else:
        n.sort()
        n2=n[len(n)-2]

    print("second larget number is: ",n2)
p = [1,2,3,4,6,7,8]
f(p)      