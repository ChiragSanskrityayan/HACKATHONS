import 

def solve():
    x = int(input())
    res = [0] * 31
    for i in range(30):
        if x & (1 << i):
            if res[i]:
                res[i + 1] = 1
                res[i] = 0
            elif i > 0:
                if res[i - 1] == 1:
                    res[i + 1] = 1
                    res[i - 1] = -1
                else:
                    res[i] = 1
            elif i == 0:
                res[i] = 1
    print(31)
    print(*res)

if __name__ == "__main__":
    random.seed(int(random.uniform(0, 1) * (10 ** 9)))
    t = int(input())
    for _ in range(t):
        solve()

