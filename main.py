import argparse

parser = argparse.ArgumentParser(description="File parser.")
parser.add_argument("--filename", "-f", required=True)
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument("--country", required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--output", "-o", required=False) # please include an output into all tasks
parser.add_argument("--total", action="store_true", required=False)
parser.add_argument("--interactive", action="store_true", required=False)

# do a separate head function?


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
                    if data[head.index("Medal")] == "Gold":
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
        if int(args.year) < 1994:
            clarification = input('Do you mean Summer or Winter Games? '
                                  'In that year both of them were held. '
                                  'Print only "Summer" or "Winter": ')
        with open(args.filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("\t")
                if is_first_line:
                    head = data
                    is_first_line = False
                    continue
                if args.year == data[head.index("Year")]:
                    country = data[head.index("Team")]
                    if int(args.year) > 1994 or clarification == data[head.index("Season")]:
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

        #table = [['Country', 'Gold', 'Silver', 'Bronze'], [country, gold_medals, silver_medals, bronze_medals]]
        #print(tabulate.tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

        for key, value in dict_medalists.items():
            print(key, ': ', value)


# TERMINAL KEY - python main.py --total --filename athlete_events.tsv --year 1972

def task3():
    pass


def task4():
    head = None
    is_first_line = True
    args = parser.parse_args()
    countrys_stats = []
    all_info = []
    first_participation = {'Country / NOC': 'Year | Type of games | Location'}
    the_most_successful = {'Country / NOC': 'The most successful games | Number of medals'}
    the_least_successful = {'Country / NOC': 'The most successful games | Number of medals'}
    average_for_games = {'Country / NOC': 'Gold | Silver | Bronze'}
    country = None
    if args.interactive:
        country = input('Enter a country or a NOC: ')
        #print(country) # + statistic
        with open(args.filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("\t")
                if is_first_line:
                    head = data
                    is_first_line = False
                    continue
                if country == data[head.index("Team")] or country == data[head.index("NOC")]:
                    info = [data[head.index("Year")], data[head.index("Games")], data[head.index("City")]]
                    if info not in all_info:
                        all_info.append(info)
                        all_info.sort()
                    #first_participation = data[head.index("Year")]
                    #the_most_successful = data[head.index("Games")]
                    #the_least_successful = data[head.index("Games")]
                        #avarage =
                    #countrys_stats.append(country)

    first_participation_stats = [all_info[0][0], all_info[0][1], all_info[0][2]]
    str_first_participation = [str(i) for i in first_participation_stats]
    first_participation.update({country: ' | '.join(str_first_participation)})
    print(f'\nThe first participation in the Olympic Games')
    for key, value in first_participation.items():
        print(key, ': ', value)
    print(f'\nThe most successful Games')
    for key, value in the_most_successful.items():
        print(key, ': ', value)
    print(f'\nThe least successful Games')
    for key, value in the_least_successful.items():
        print(key, ': ', value)
    print(f'\nThe average of medals per Games')
    for key, value in average_for_games.items():
        print(key, ': ', value)


# TERMINAL KEY - python main.py --interactive -f athlete_events.tsv


def main():
    task1()
    task2()
    #task3()
    #task4()


if __name__ == "__main__":
    main()
