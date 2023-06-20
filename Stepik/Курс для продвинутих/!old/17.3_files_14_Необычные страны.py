# with open('17.3_files_14_Необычные страны.txt', 'r') as countries_file:
#     countries_list = [line.strip().split('\t') for line in countries_file.readlines()]
#
# filtered_countries_list = [country for country in countries_list if country[0].startswith('G') and int(country[-1]) > 500_000]
# for country in filtered_countries_list:
#     print(country[0])

with open('17.3_files_14_Необычные страны.txt', 'r') as countries_file:


    countries_dict = {key: int(value) for key, value in (tuple(country.strip().split('\t')) for country in countries_file.readlines())}

filtered_countries_list = [country for country, popul in countries_dict.items() if country.startswith('G') and popul > 500_000]
for country in filtered_countries_list:
    print(country)
