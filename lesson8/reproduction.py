organism = [1, 2, [4, 5], 'eyes']
organism_copy = organism.copy()
organism.extend(organism_copy)
print(organism)
