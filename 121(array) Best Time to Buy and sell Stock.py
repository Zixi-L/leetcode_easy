prices = [7,5,10,7,1,4,9]

# solution1
# The complexity is: O(n2)
max_profit = 0
for i in range(len(prices)):
    min_s = prices[i]
    print('I am min_s: ', min_s)
    for s in prices[i+1::]:
        print('start printing s: ', s)
        if s > min_s:
            min_s = s
            profit = min_s - prices[i]
            if profit > max_profit:
                max_profit = profit
    
print(max_profit)

# Solution2
# The complexity is O(n)
# float('inf') means a value that is ∞ (infinity)
# 画一个价格波动图。然后 buy_price 会停在谷底或者更低的谷底。 res记录顶峰和谷底的差。最终return最大利润

buy_price , res = float('inf'), 0 
for p in prices:
    buy_price = min(p, buy_price) # keep tracking the lowest buy price
    res  = max(res, p - buy_price) 
print(res)

