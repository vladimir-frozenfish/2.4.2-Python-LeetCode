def maximumWealth(accounts):
    return max([sum(i) for i in accounts])

lists = [[2,8,7],[7,1,3],[1,9,5]]
print(maximumWealth(lists) == 17)

