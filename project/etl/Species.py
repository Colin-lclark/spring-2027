def Species():
    specset = set()
    with open('/Users/Colin/spring-2026/Tree Database/Tree_Records.csv') as rows:
        for line in rows:
            species = line[line.find(' - ') + 3:line.find(',')]
            specset.add(species)
    return specset

def numSpecies(setspec):
    spec = 0
    for species in setspec:
        spec += 1
    return spec

print(numSpecies(Species()))