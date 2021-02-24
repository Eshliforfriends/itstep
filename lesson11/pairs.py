biggest_cities = ['Tokyo', 'Delhi', 'Shanghai','Mexcio City', 'Sao Paulo'
                  'Mumbai', 'Kinki major metropolitan area', 'Cairo']
pairs = map(lambda city: f' {biggest_cities[biggest_cities.index(city)]}, {biggest_cities.index(city) +1}'
            if city in biggest_cities else None, biggest_cities)

print(list(pairs))
