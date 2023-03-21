import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
data = response.json()
for i in data:
    if 'Hulk' == i.get('name'):
        name_1 = i.get('name')
        intelligence_1 = i.get('powerstats').get('intelligence')
        print('У', name_1, 'интеллект равен:',intelligence_1 )
    elif 'Captain America' == i.get('name'):
        name_2 = i.get('name')
        intelligence_2 = i.get('powerstats').get('intelligence')
        print('У', name_2, 'интеллект равен:', intelligence_2)
    elif 'Thanos' == i.get('name'):
        name_3 = i.get('name')
        intelligence_3 = i.get('powerstats').get('intelligence')
        print('У', name_3, 'интеллект равен:', intelligence_3)
if intelligence_2 < intelligence_1 > intelligence_3:
    print('Самый умный супергерой это', name_1)
elif intelligence_1 < intelligence_2 > intelligence_3:
    print('Самый умный супергерой это', name_2)
elif intelligence_2 < intelligence_3 > intelligence_1:
    print('Самый умный супергерой это', name_3)
elif intelligence_2 == intelligence_1 == intelligence_3:
    print('Самый умный супергерой не выявлен!')
