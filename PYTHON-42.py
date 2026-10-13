i=1
while i<=15:
    if(i%2==0):
        i+=1
        continue #skip
    print(i)
    i+=1

    list=[1,2,3,4,5,6,7,8,9]
    for num in list:
        if num%3==0:
            continue #skip
        print(num)
        ladies=["sughra","yasmeen","humaira"]
        for value in ladies:
            if value=="yasmeen":
                continue #skip
            print(value)
