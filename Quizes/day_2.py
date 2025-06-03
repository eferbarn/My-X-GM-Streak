def is_magical(n):
    digits = [int(d) for d in str(n)]
    return sum(d**3 for d in digits) == n


if __name__ == "__main__":
    for i in range(100, 1000):
        if is_magical(i):
            print(i)
