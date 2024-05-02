#Sports day

def max_efficiency(num):
    num.sort()
    n = len(num)
    max_effi = 0

    for i in range(n):
        effi = 0
        p= 1

        for j in range(i,n):
            effi += num[j] * p
            p+= 1

            if effi > max_effi:
                max_effi = effi

    return max_effi

#ip
num= list(map(int, input().split()))

#op
res = max_efficiency(num)
print(res if res > 0 else 0)