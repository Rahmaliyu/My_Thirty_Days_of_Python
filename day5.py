empty_list = list()

Items = ['Goat', 'Yam', 'Road', 'Zebra', 'House']

print(len(Items))

first_item = Items[0]
print(' the first tem on the list is ', first_item)
median = len(Items)
middle_item =Items[median // 2]
print('the middle item is ', middle_item)
last_item = Items[-1]
print('the last item is', last_item)

mixed_data_types = ['Rahma', 90, 5.68, 'single', 'janbulo kabuga housing estate kano']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM','Oracle','Amazon']

print(it_companies)
print(len(it_companies))

first_it = it_companies[0]
middle_comp = len(it_companies)
middle_it = it_companies[middle_comp // 2]
last_it = it_companies[-1]
print( f'the first It company is {first_it},the middle company is {middle_it} and the last company is {last_it}')
it_companies[0] = 'Instagram'
print(it_companies)
it_companies.append('Snapchat')
print(it_companies)
it_companies.insert(4, 'Facebook')
print(it_companies)
it_companies[0] = it_companies[0].upper()
print( 'First company in c',it_companies)

joined_companies = '#;&nbsp; '.join(it_companies)
print(joined_companies)


exist = 'Microsoft' in it_companies
print( 'does Microsoft exist in list of companies ?',exist)

it_companies.sort()
print("sorted list of companies ", it_companies)

it_companies.reverse()
print('companies in reverse ',it_companies)

first3 = it_companies[:3]
print('first three companies ', first3)

last3 = it_companies[6:]
print( ('the last three campanies are'), last3)

no_of_companies = len(it_companies)
middle = it_companies[no_of_companies // 2]
print('The middle company is ', middle)

it_companies.pop(0)
del it_companies[3:5]
it_companies.pop()
print(('the companies list after deleting some companies '),it_companies)
it_companies.clear()
print('IT companies after clearing ', it_companies)
del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

print(front_end)
full_stack = front_end.copy()
front_end.insert(5,'python')
front_end.insert(6, 'SQL')
print(front_end)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
minimun_Age = min(ages)
maxaimum_Age = max(ages)
print('the minumum age is', minimun_Age)
print('the maximum age is ', maxaimum_Age)
total_No_of_ages = len(ages)
if total_No_of_ages % 2 == 0:
    first_median = ages[total_No_of_ages //2]
    second_median = ages[total_No_of_ages //2 - 1]

    median_age = (first_median + second_median)/2
else:
    median_age = ages[total_No_of_ages // 2]

print('the median age is ', median_age)

ages.append(maxaimum_Age)
print('the list after adding maximum age', ages)
ages.append(minimun_Age)
print('the list after adding minimum age', ages)
sum_ages = sum(ages)
print('the sum of all ages is  ', sum_ages)

average_age = sum_ages / total_No_of_ages
print('the average  age is ', average_age)
range_of_ages = maxaimum_Age - minimun_Age
print('the range of the age is ', range_of_ages)




countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];


middle_coutry = len(countries)
middle_country = countries [middle_coutry // 2]
print(' The middle country is ', middle_country)

first_half_contries = middle_coutry // 2
first_half = countries[:first_half_contries]
print(first_half)

seond_half_countries = countries[first_half_contries:]
print(seond_half_countries)

countries_2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
chn, rus, us, *scadic = countries_2




