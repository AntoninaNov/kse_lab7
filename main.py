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
        gold_medals = 0
        silver_medals = 0
        bronze_medals = 0
        medalists = 0
        store = {}
        # if args.output is not None:
        #     output_file = open(args.output, "w")
        with open(args.filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("\t")
                if is_first_line:
                    head = data
                    is_first_line = False
                    continue

                if args.country == data[head.index("NOC")] and args.year == data[head.index("Year")]:
                    if data[head.index("Medal")]  == "Gold":
                        gold_medals += 1
                    elif data[head.index("Medal")] == "Silver":
                        silver_medals += 1
                    elif data[head.index("Medal")] == "Bronze":
                        bronze_medals += 1
        print(f'The quantity of medals of {args.country} medalists in {args.year}:\nGold: {gold_medals};\nsilver: {silver_medals};\nbronze: {bronze_medals}.\n')
        #             if output_file is not None:
        #                 idx += 1
        #                 output_file.write(str(idx) + ",".join(data) + "\n")
        #
        # if output_file is not None:
        #     output_file.close()
    # файл для виведення результатів (output_file)

def task2():
    head = None
    is_first_line = True
    args = parser.parse_args()
    countries_medalists = []
    dict_medalists = {'Country': 'Gold | Silver | Bronze'}
    country_and_type_of_medal = []
    if args.total:
        #output_file = None
        #idx = 0
        #if args.output is not None:
            #output_file = open(args.output, "w")
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
                        each_participants_country_and_medal = [data[head.index("Team")], data[head.index("Medal")]]
                        country_and_type_of_medal.append(each_participants_country_and_medal)
                        country_and_type_of_medal.sort()
                        if country not in countries_medalists:
                            countries_medalists.append(country)
                            countries_medalists.sort()

        for country in countries_medalists:
            gold_medals = 0
            silver_medals = 0
            bronze_medals = 0
            for m in range(len(country_and_type_of_medal)):
                if country == country_and_type_of_medal[m][0]:
                    if country_and_type_of_medal[m][1] == 'Gold':
                        gold_medals = gold_medals + 1
                    elif country_and_type_of_medal[m][1] == 'Silver':
                        silver_medals = silver_medals + 1
                    elif country_and_type_of_medal[m][1] == 'Bronze':
                        bronze_medals = bronze_medals + 1
                medals = [gold_medals, silver_medals, bronze_medals]
                str_medals = [str(i) for i in medals]
                dict_medalists.update({country: ' | '.join(str_medals)})

        for key, value in dict_medalists.items():
            print(key, ': ', value)

#TERMINAL KEY - python main.py --total --filename athlete_events.tsv --year 1972

def task3():
    pass


def task4():
    pass


def main():
    #task1()
    task2()


if __name__ == "__main__":
    main()
