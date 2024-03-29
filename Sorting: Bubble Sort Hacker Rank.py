def countSwaps(a):
    count=0
    for i in range(n):
        for j in range(n-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                count += 1
    print("Array is sorted in",end=" ")
    print(count,end=" ")
    print("swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])  
