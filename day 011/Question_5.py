from country_data import countries_data
def most_spoken_languages():

    languages = []
    for i in range(len(countries_data)):
      languages.extend(countries_data[i]['languages'])

    lang = {}
    for language in languages:
        lang[language] = lang.get(language,0) + 1


    sorted_lang = sorted(lang.items(), key= lambda x:x[1],reverse=True)
    sorted_lang 
    top_ten = []
    for i in range(10):
       top_ten.append(sorted_lang[i])
    return top_ten

print(f'Ten most spoken languages:  {most_spoken_languages()}')



def most_populated_countries():
    population = {}
    for i in range(len(countries_data)):
        keys = countries_data[i]['name']
        values = countries_data[i]['population']
        population[keys] = values
    sorted_pop = sorted(population.items(), key= lambda x:x[1],reverse=True)

    most_pop = []
    for i in range(10):
        most_pop.append(sorted_pop[i][0])

    return most_pop

print(f'Ten most populated countries: {most_populated_countries()}')