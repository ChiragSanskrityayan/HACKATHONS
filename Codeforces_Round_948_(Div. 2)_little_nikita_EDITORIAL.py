
def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        print("Yes" if n >= m and n % 2 == m % 2 else "No")


main()
