list=list(map(int,input().split()))

while 1:
    for i in list:
        if i%2==0:
            print("even")
        else:
            print("odd")
    break