candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))

s = 0
a= max(candles)
for i in range(len(candles)):
    if(candles[i]== a):
        s+=1

print(s)
