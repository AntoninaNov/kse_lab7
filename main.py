import argparse
from typing import List
import tabulate

parser = argparse.ArgumentParser(description="File parser.")
parser.add_argument("--filename", "-f", required=True)
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument('--country', nargs='+', required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--output", required=False) # please include an output into all tasks
parser.add_argument("--total", action="store_true", required=False)
parser.add_argument('--overall', nargs="*")
parser.add_argument("--interactive", action="store_true", required=False)


# do a separate head function?


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
    head = None
    is_first_line = True
    args = parser.parse_args()
    countries_medalists = []
    dict_medalists = {}
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
                            if country not in countries_medalists:
                                countries_medalists.append(country)
                            #country_and_type_of_medal.sort()
                            #countries_medalists.sort()
                            else:
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
                                            dict_medalists.update({country: [gold_medals, silver_medals, bronze_medals]})

        sorted_dict = sorted(dict_medalists.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_dict)
        headers = ['Country', 'Gold', 'Silver', 'Bronze']
        table = []
        for key, value in converted_dict.items():
            table.append([key, value[0], value[1], value[2]])
        print(tabulate.tabulate(table, headers=headers, tablefmt='fancy_grid'))
m
# TERMINAL KEY - python main.py --total --filename athlete_events.tsv --year 1972


def task3():
    head = None
    is_first_line = True
    args = parser.parse_args()
    if args.overall:
        overall_countries = [{} for x in args.overall]
        with open(args.filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("\t")
                if is_first_line:
                    head = data
                    is_first_line = False
                    continue

                if args.overall and data[head.index("Medal")] != 'NA\n':
                    for i, country in enumerate(args.overall):
                        if country in data:
                            if data[head.index("Year")] not in overall_countries[i]:
                                overall_countries[i][data[head.index("Year")]] = 1
                            else:
                                overall_countries[i][data[head.index("Year")]] += 1
        max_overall_countries = ""
        min_overall_countries = ""
        average_overall_countries = ""
        for i in range(len(overall_countries)):
            numbers_of_medals = [int(x) for x in overall_countries[i].values() if int(x) != 0]
            max_value = max(numbers_of_medals)
            min_value = min(numbers_of_medals)
            average_value = round(sum(numbers_of_medals)/len(numbers_of_medals))
            years_of_medals = [x for x in overall_countries[i].keys()]
            max_year = years_of_medals[numbers_of_medals.index(max_value)]
            min_year = years_of_medals[numbers_of_medals.index(min_value)]

            max_overall_countries += f'{args.overall[i]} - year {max_year} - {max_value} medals\n'
            min_overall_countries += f'{args.overall[i]} - year {min_year} - {min_value} medal(s)\n'
            average_overall_countries += f'In average {args.overall[i]} has received {average_value} medals\n'

        print(max_overall_countries)
        print(min_overall_countries)
        print(average_overall_countries)


def task4():
    head = None
    is_first_line = True
    args = parser.parse_args()
    country = None
    first_year = None
    first_season = None
    first_location = None
    countrys_stats = []
    all_info = []
    least_successful_year = None
    most_successful_year = None
    #first_participation = {}
    #the_most_successful = {'Country / NOC': 'The most successful games | Number of medals'}
    #the_least_successful = {'Country / NOC': 'The most successful games | Number of medals'}
    #average_for_games = {'Country / NOC': 'Gold | Silver | Bronze'}
    all_participations = []
    all_years_and_medals = []
    counted_medals_per_games = {}
    all_years = []

    if args.interactive:
        country = input('Enter a country or a NOC: ')
        # print(country) # + statistic
        with open(args.filename, "r") as file:
            for line in file.readlines():
                data = line.strip().split("\t")
                if is_first_line:
                    head = data
                    is_first_line = False
                    continue
                if country == data[head.index("Team")] or country == data[head.index("NOC")]:
                    year = data[head.index("Year")]
                    season = data[head.index("Season")]
                    location = data[head.index("City")]
                    medal = data[head.index("Medal")]
                    participation = [year, season, location]
                    year_medal = [year, medal]
                    all_years_and_medals.append(year_medal)
                    if participation not in all_participations:
                        all_participations.append(participation)
                        all_years.append(year)
                    else:
                        for each_year in all_years:
                            gold_medals = 0
                            silver_medals = 0
                            bronze_medals = 0
                            for n in range(len(all_years_and_medals)):
                                if each_year == all_years_and_medals[n][0]:
                                    if all_years_and_medals[n][1] == 'Gold':
                                        gold_medals = gold_medals + 1
                                    elif all_years_and_medals[n][1] == 'Silver':
                                        silver_medals = silver_medals + 1
                                    elif all_years_and_medals[n][1] == 'Bronze':
                                        bronze_medals = bronze_medals + 1
                                    counted_medals_per_games.update({each_year: [gold_medals, silver_medals, bronze_medals]})

        #print(tabulate.tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        all_participations.sort()  # Сортуємо за першим значенням - за роком
        print(all_participations)
        #first_participation = all_participations[0]  # а [0] - найменший рік
        first_year = all_participations[0][0]
        first_season = all_participations[0][1]
        first_location = all_participations[0][2]

        print(f'\nThe first participation in the Olympic Games')
        table_first_participation = [['Year', 'Season of games', 'Location'], [first_year, first_season, first_location]]
        print(tabulate.tabulate(table_first_participation, headers='firstrow', tablefmt='fancy_grid'))

        sorted_dict = sorted(counted_medals_per_games.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_dict)

        successful = list(converted_dict.items())[0]
        #print(type(successful))
        #print(successful)
        print(f'\nThe most successful Games')
        table_most_successful = ['Games', 'Gold', 'Silver', 'Bronze'], [successful[0], successful[1][0], successful[1][1], successful[1][2]]
        print(tabulate.tabulate(table_most_successful, headers='firstrow', tablefmt='fancy_grid'))

        unsuccessful = list(converted_dict.items())[-1]
        print(f'\nThe least successful Games')
        table_least_succesful = ['Games', 'Gold', 'Silver', 'Bronze'], [unsuccessful[0], unsuccessful[1][0], unsuccessful[1][1], unsuccessful[1][2]]
        print(tabulate.tabulate(table_least_succesful, headers='firstrow', tablefmt='fancy_grid'))

        print(f'\nThe average of medals per Games')
        table_average_medals = [['Gold', 'Silver', 'Bronze', 'Total'], []]
        print(tabulate.tabulate(table_average_medals, headers='firstrow', tablefmt='fancy_grid'))


# TERMINAL KEY - python main.py --interactive -f athlete_events.tsv


def main():
    task1()
    # task2()
    # task3()
    # task4()


if __name__ == "__main__":
    main()
