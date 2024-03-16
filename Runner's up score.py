if __name__ == '__main__':
    n = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    winner=A[0]
    for i in range(len(A)):
        if A[i]!= winner:
            print(A[i])
            break
