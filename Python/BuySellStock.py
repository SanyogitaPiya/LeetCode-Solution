def maxProfit(prices):
    sm = prices[0]
    prev_diff = 0
    for i in range(1,len(prices)):
        if(sm < prices[i]):
            diff = prices[i]-sm
            if(prev_diff<diff):
                prev_diff = diff
        else:
            sm = prices[i]
    return prev_diff

prices = [2,4,1]
print(maxProfit(prices))