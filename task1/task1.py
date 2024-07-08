import sys


def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    current_index = 0
    path = []
    arr = [i for i in range(1, n + 1)]
    # print(arr)
    while True:
        path.append(arr[current_index])
        current_index = (current_index + m) % n - 1

        if current_index == 0:
            break
    print("".join(map(str, path)))


if __name__ == "__main__":
    main()
