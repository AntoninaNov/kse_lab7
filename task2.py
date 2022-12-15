import argparse

parser = argparse.ArgumentParser(description="File parser.")
parser.add_argument("--filename", "-f", required=True)
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument("--country", required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--output", "-o", required=False) # please include an output into all tasks
parser.add_argument("--total", action="store_true", required=False)


def task2():
    head = None
    is_first_line = True
    args = parser.parse_args()
    countries_medalists = []
    if args.total:
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
                if args.year == data[head.index("Year")]:
                    country = data[head.index("Team")]
                    if data[head.index("Medal")] != "NA":
                        if country not in countries_medalists:
                            countries_medalists.append(country)
                            countries_medalists.sort()

            country_and_medals = []
            gold_medals = 0
            silver_medals = 0
            bronze_medals = 0
            for n in range(len(countries_medalists)):
                team = countries_medalists[n]
                country_and_medals.append(team)
                for line in file.readlines():
                    if team == data[head.index("Team")]:
                        if data[head.index("Medal")] == "Gold":
                            gold_medals = gold_medals + 1
                        elif data[head.index("Medal")[line]] == "Silver":
                            silver_medals = silver_medals + 1
                        elif data[head.index("Medal")[line]] == "Bronze":
                            bronze_medals = bronze_medals + 1
                country_and_medals.append(gold_medals)
                country_and_medals.append(silver_medals)
                country_and_medals.append(bronze_medals)
                print(country_and_medals)
                country_and_medals.clear()
        print(", ".join(countries_medalists))


#python task2.py --total --filename athlete_events.tsv --year 1972



def main():
    task2()


if __name__ == "__main__":
    main()
