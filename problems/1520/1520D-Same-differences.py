def solve(arr):
    hash_map = {}
    for i, c in enumerate(arr):
        hash_map[c - i] = hash_map.get(c - i, 0) + 1
    # print(hash_map)

    count = 0
    for k in hash_map:
        n = hash_map[k]
        count += (n * (n - 1) // 2)

    print(count)


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr)
        i += 1