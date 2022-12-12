import sys

def task1(filename, country, year):
    head = None
    is_first_line = True
    with open(filename, "r") as file:
        for line in file.readlines():
            data = line.strip().split("\t")
            if is_first_line:
                head = data
                is_first_line = False
                continue
            if country == data[head.index("NOC")] and year == data[head.index("Year")]:
                pass


def task2():
    pass

def main():
    args = sys.argv
    if args[1] == "-medals":
        filename = args[args.index("-filename") + 1]
        country = args[args.index("-country") + 1]
        year = args[args.index("-year") + 1]
        print(filename, country, year)
        task1(filename, country, year)


if __name__ == "__main__":
    main()
