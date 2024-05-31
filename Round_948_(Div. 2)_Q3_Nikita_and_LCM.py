from math import gcd

def lcm(a, b):
    return (a // gcd(a, b)) * b

def main():
    t = int(input())
    #t = 1

    while t > 0:
        n = int(input())

        vec = list(map(int, input().split()))
        mp = {}
        for num in vec:
            mp[num] = mp.get(num, 0) + 1

        lcm_org = -1
        maxx = 0

        for i in range(n):
            if lcm_org == -1:
                lcm_org = vec[i]
            else:
                lcm_org = lcm(lcm_org, vec[i])

            if lcm_org > 10**9 or lcm_org < 0:
                maxx = n
                break

        if lcm_org > 10**9 or lcm_org < 0 or lcm_org not in mp:
            maxx = n
            print(maxx)
            t -= 1
            continue

        for i in range(1, int(lcm_org ** 0.5) + 1):
            cnt = 0
            lcm_check = -1
            if i not in mp:
                for j in range(n):
                    if i % vec[j] == 0:
                        cnt += 1
                        if lcm_check == -1:
                            lcm_check = vec[j]
                        else:
                            lcm_check = lcm(lcm_check, vec[j])

                        if lcm_check > i:
                            break
                if lcm_check == i:
                    maxx = max(maxx, cnt)

            cnt = 0
            lcm_check = -1
            if lcm_org // i not in mp:
                for j in range(n):
                    if (lcm_org // i) % vec[j] == 0:
                        cnt += 1
                        if lcm_check == -1:
                            lcm_check = vec[j]
                        else:
                            lcm_check = lcm(lcm_check, vec[j])

                        if lcm_check > lcm_org // i:
                            break
                if lcm_check == lcm_org // i:
                    maxx = max(maxx, cnt)

        print(maxx)
        t -= 1

if __name__ == "__main__":
    main()

