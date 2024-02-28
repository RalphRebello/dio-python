T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    cheias = 0
    while N >= K:
        cheias += 1
        N -= K
    print(cheias + N)
        