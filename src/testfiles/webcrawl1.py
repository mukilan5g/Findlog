with open('q1-cities1.txt','r') as f:
    while f.readline() != '':
        cities_list1.append(f.readline())
with open('q1-cities2.txt','r') as f:
    while f.readline() != '':
	    cities_list2.append(f.readline())

cities_in_both = []
cities_not_in_cities_list2 = []
cities_in_either_one = []

for city in cities_list1:
    if city in cities_list2:
	    cities_in_both.append(city)
		
    if city not in cities_list2:
        cities_not_in_cities_list2.append(city)
		
    if city in (cities_list2 or cities_list1):
        cities_in_either_one.append(city)
		
print 'cities in both:\n',cities_in_both
print 'cities in file1:\n',cities_not_in_cities_list2
print 'cities in Either one:\n',cities_in_either_one