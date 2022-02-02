import csv
import json
from unicodedata import name
from urllib.request import urlopen

url = 'http://api.football-data.org/v2/competitions/'
football_data = json.load(urlopen(url))

tier_choice = input('Please enter the tier you want to extract (1 to 4 only): ')

with open("Football-Competitions.csv", 'w', newline='') as fil:
    fieldNames = ['Id', 'Name', 'Area/Country', 'Available Seasons', 'Tier']
    filewriter = csv.DictWriter(fil, fieldnames=fieldNames)

    filewriter.writeheader()
    for comp in football_data['competitions'] :
        if tier_choice == '1':
            if comp['plan'] == 'TIER_ONE':
                filewriter.writerow({'Id': comp['id'], 'Name': comp['name'], 'Area/Country': comp['area']['name'], 'Available Seasons': comp['numberOfAvailableSeasons'], 'Tier': comp['plan']})
        elif tier_choice == '2':
            if comp['plan'] == 'TIER_TWO':
                filewriter.writerow({'Id': comp['id'], 'Name': comp['name'], 'Area/Country': comp['area']['name'], 'Available Seasons': comp['numberOfAvailableSeasons'], 'Tier': comp['plan']})
        elif tier_choice == '3':
            if comp['plan'] == 'TIER_THREE':
                filewriter.writerow({'Id': comp['id'], 'Name': comp['name'], 'Area/Country': comp['area']['name'], 'Available Seasons': comp['numberOfAvailableSeasons'], 'Tier': comp['plan']})
        elif tier_choice == '4':
            if comp['plan'] == 'TIER_FOUR':
                filewriter.writerow({'Id': comp['id'], 'Name': comp['name'], 'Area/Country': comp['area']['name'], 'Available Seasons': comp['numberOfAvailableSeasons'], 'Tier': comp['plan']})
        else:
            print('ERROR!! There are only FOUR TIERS available.')