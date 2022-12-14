import sys
import argparse

parser = argparse.ArgumentParser(description="File parser.")
parser.add_argument("--filename", "-f", required=True)
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument("--country", required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--output", "-o", required=False) # please include an output into all tasks
parser.add_argument("--total", action="store_true", required=False)


def task1():
    head = None
    is_first_line = True
    args = parser.parse_args()
    if args.medals:
        output_file = None
        idx = 0
        if args.output is not None:
            output_file = open(args.output, "w")
        with open(args.filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("\t")
                if is_first_line:
                    head = data
                    is_first_line = False
                    continue
                if args.country == data[head.index("NOC")] and args.year == data[head.index("Year")]:
                    print(line.strip())
                    if output_file is not None:
                        idx += 1
                        output_file.write(str(idx) + ",".join(data) + "\n")
        if output_file is not None:
            output_file.close()
    # файл для виведення результатів (output_file)


def task2():
    pass


def task3():
    pass


def task4():
    pass


def main():
    task1()


if __name__ == "__main__":
    main()
