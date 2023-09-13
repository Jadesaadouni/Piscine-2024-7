import json


Prizes=open('nobelprizes.json')

data = json.load(Prizes)

u_category = set()
for i in data ['prizes']:
    category = i['category']
    u_category.add(category)

category_list= list(u_category) 
#print(category_list)

Prizes.close()

Laureates=open('nobelLaureates.json')

data_laureates = json.load(Laureates)

u_firstname = set()
for i in data_laureates['laureates']:
    #print (i['firstname'])
    firstname=i['firstname']
    u_firstname.add(firstname)
Laureates_list= list(u_firstname)
sorted_firstname= sorted(Laureates_list)
#print(sorted_firstname)
Laureates.close()

nb_countries = open('nobelCountries.json')

data_countries = json.load(nb_countries)

country_list = [(entry['name'], entry.get('code', None)) for entry in data_countries['countries']]

print(country_list)

nb_countries.close()
