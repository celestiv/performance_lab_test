import sys


def main():
    input_file = sys.argv[1]
    nums = []
    with open(input_file, "r") as nums_file:
         nums = list(map(int, nums_file.readlines()))
    nums_mean = round(sum(nums) / len(nums))
    result = 0
    for i in nums:
        result += abs(nums_mean - i)
    print(result)

if __name__ == "__main__":
    main()
