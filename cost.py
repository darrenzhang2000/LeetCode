import copy
def func(cost):
    memo = copy.deepcopy(cost)
    for i in range(1, len(cost)):
        memo[i][0] = min(memo[i - 1][1], memo[i - 1][2]) + cost[i][0]
        memo[i][1] = min(memo[i - 1][0], memo[i - 1][2]) + cost[i][1]
        memo[i][2] = min(memo[i - 1][0], memo[i - 1][1]) + cost[i][2]
    return min(memo[-1]) 

def func2(cost):
    m0, m1, m2 = cost[0]
    for i in range(1, len(cost)):
        new_m0 = cost[i][0] + min(m1, m2)
        new_m1 = cost[i][1] + min(m0, m2)
        new_m2 = cost[i][2] + min(m0, m1)
        m0, m1, m2 = new_m0, new_m1, new_m2
    return min(m0, m1, m2)

cost = [
    [1, 2, 3],
    [1, 2, 3],
    [3, 3, 1]
]

# print(func2(cost))

# def func3(weights, maxCapacity):
