import sys
import math


def read_coordinates(coordinates_file_path):
    coordinates_arr = []
    with open(coordinates_file_path, "r") as coord:
        for line in coord.readlines():
            coordinates_arr.append(list(map(int, line.strip().split(" "))))
    return coordinates_arr


def read_dots(dots_file_path):
    dots_arr = []
    with open(dots_file_path, "r") as dots:
        for dotline in dots.readlines():
            dots_arr.append(list(map(int, dotline.strip().split(" "))))
    return dots_arr


def calculate(coordinates_arr, dots_arr):
    output = []
    for dot in dots_arr:
        result = math.sqrt(( (dot[0] - coordinates_arr[0][0]) ** 2) + ((dot[1] - coordinates_arr[0][1]) ** 2) )

        if result < coordinates_arr[1][0]:
            output.append(1)
        elif result == coordinates_arr[1][0]:
            output.append(0)
        else:
            output.append(2)
    return output


def main():
    if len(sys.argv) == 3:
        
        coordinates_file_path = sys.argv[1]
        dots_file_path = sys.argv[2]

        coordinates_arr = read_coordinates(coordinates_file_path)
        dots_arr = read_dots(dots_file_path)

        output = calculate(coordinates_arr, dots_arr)

        print(*output, sep="\n")
    else:    
        print("Передайте файлы в качетсве аргументов!")


if __name__ == "__main__":
    main()
