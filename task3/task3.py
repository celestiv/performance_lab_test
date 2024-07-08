import json
import sys


def read_files():
    values = {}
    tests = {}

    with open(sys.argv[1], "r") as values_file:
        values = json.load(values_file)
    with open(sys.argv[2], "r") as tests_file:
        tests = json.load(tests_file)
    return values, tests
    

def update_values(tests, values):
    for test in tests:
        if "id" in test:
            for value in values["values"]:
                if test["id"] == value["id"]:
                    test["value"] = value["value"]
        if "values" in test:
            update_values(test["values"], values)
    return tests


def main():
    if len(sys.argv) == 4:
        values, tests = read_files()
        output = sys.argv[3]
        result = update_values(tests["tests"], values)
        with open(output, "w") as output_file:
            json.dump({"tests": result}, output_file, indent=2)
    else:
        print("Нужно передать файлы для считывания! ")


if __name__ == "__main__":
    main()
