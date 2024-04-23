def linear(l,k):
    for i, e in enumerate(l):
        if k==e:
            print("item found at",i+1)
            break
    else:
        print("item not found")
linear([1,2,3,4],3)