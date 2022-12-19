import sys
import argparse
import tabulate

parser = argparse.ArgumentParser(description="File parser.")
parser.add_argument("--filename", "-f", required=True)
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument("--country", required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--output", required=False) # please include an output into all tasks
parser.add_argument("--total", action="store_true", required=False)
parser.add_argument('--overall', nargs="*")


def task1():
    head = None
    is_first_line = True
    args = parser.parse_args()
    if args.medals:
        output_file = None
        gold_medals = 0
        silver_medals = 0
        bronze_medals = 0
        medalists = {}
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
                    if len(medalists) < 10 and data[head.index("Medal")] != "NA":
                        medalists[data[head.index("Name")]] = data[head.index("Medal")]
                        headers = ['Name', 'Sport', 'Medal']
                        medalists[data[head.index("Name")]] = data[head.index("Sport")], data[head.index("Medal")]
                    if data[head.index("Medal")] == "Gold":
                        gold_medals += 1
                    elif data[head.index("Medal")] == "Silver":
                        silver_medals += 1
                    elif data[head.index("Medal")] == "Bronze":
                        bronze_medals += 1

        print(f'The quantity of medals of {args.country} medalists in {args.year}:')
        medals_table_values = [['Gold', 'Silver', 'Bronze'], [gold_medals, silver_medals, bronze_medals]]
        medals_table = tabulate.tabulate(medals_table_values, headers='firstrow')
        print(medals_table)
        medalists_table = tabulate.tabulate([(k,) + v for k, v in medalists.items()], headers=headers)
        print(medalists_table)
        if output_file is not None:
            output_file.write(medals_table)

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
