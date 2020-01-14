def pascalTriangle(n):
    k = 2*n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1

        for j in range(0,i+1):
            print(function(i,j), end=" ")
        print("\r")

def function(a,b):
    res = 1
    for i in range(0,b):
        res = res*(a-i)
        res = res//(i+1)
    return res

pascalTriangle(10)