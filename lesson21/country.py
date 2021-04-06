class Country:
    country_name = None
    capital = None
    continent = None
    population = None
    cities = None

    def __init__(self, country_name, capital, continent, population, cities):
        if type(country_name) == str:
            self.country_name = country_name
        else:
            self.country_name = None
        if type(capital) == str:
            self.capital = capital
        else:
            self.capital = None
        if type(continent) == str:
            self.continent = continent
        else:
            self.continent = None
        if type(population) == int:
            self.population = population
        else:
            self.population = None
        if type(cities) == str:
            self.cities = cities
        else:
            self.cities = None

    def __str__(self):
        return f'Cuontry: {self.country_name} \nCapital is {self.capital} \nCountry is on continent {self.continent} \nPopulation is {self.population} million \nCities are {self.cities} '

if __name__ == '__main__':
    elem = Country('Japan', 'Tokyo', 'Asia', 55 , 'Osaka, Okayama, Kioto')
    print(elem)