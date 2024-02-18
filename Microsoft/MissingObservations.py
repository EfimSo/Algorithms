# generate an array of length n such that
# 1. The sum of the array is 
# mean = (sum(rolls) + sum(output)) / (n + m)
# mean * (n + m) = sum(rolls) + sum(output)
# (n+m)mean - sum(rolls) = sum(output)

def missingRolls(rolls: list[int], mean: int, n: int) -> list[int]:
    m, sm = len(rolls), sum(rolls)
    sn = (n + m) * mean - sm
    if sn < n or sn > 6 * n:
        return []
    part, rem = divmod(sn, n)
    res = [part] * n
    # By Euclidian division, rem < n
    for i in range(rem):
        res[i] += 1
    return res



        