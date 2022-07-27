wt = [1, 2, 3, 4]
value = [50, 200, 150, 100]
capacity = 7


def knapsack(wt, value, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if wt[n-1] > capacity:
        return knapsack(wt, value, capacity, n-1)
    else:
        return max(value[n-1]+knapsack(wt, value, capacity-wt[n-1], n-1), knapsack(wt, value, capacity, n-1))


ans = knapsack(wt, value, capacity, 4)
print(ans)
