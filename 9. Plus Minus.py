n = int(input())

arr = [1 if int(temp)>0 else -1 if int(temp)<0 else 0 for temp in input().split(' ') ]
print("{0:.6f}".format(arr.count(1)/n))
print("{0:.6f}".format(arr.count(-1)/n))
print("{0:.6f}".format(arr.count(0)/n))
