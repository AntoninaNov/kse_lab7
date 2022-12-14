import sys
import argparse

def task1():
    parser = argparse.ArgumentParser(description="Medals parser.")
    parser.add_argument("--filename", "-f", required=True)
    parser.add_argument("--medals", action="store_true", required=False)
    parser.add_argument("--country", required=False)
    parser.add_argument("--year", required=False)
    parser.add_argument("--output", "-o", required=False)
    head = None
    is_first_line = True
    args = parser.parse_args()
    if args.medals:
        with open(args.filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("\t")
                if is_first_line:
                    head = data
                    is_first_line = False
                    continue
                if args.country == data[head.index("NOC")] and args.year == data[head.index("Year")]:
                    print(line.strip())


def task2():
    parser = argparse.ArgumentParser(description="Total parser.")
    parser.add_argument("--filename", "-f", required=True)
    parser.add_argument("--total", action="store_true", required=False)
    parser.add_argument("--output", "-o", required=False)  # please include an output into all tasks

def task3():
    parser = argparse.ArgumentParser(description="Overall parser.")

def task4():
    parser = argparse.ArgumentParser(description="Interactive parser.")

def main():
    task1()


if __name__ == "__main__":
    main()
