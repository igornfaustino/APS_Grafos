import get_data
import graph
import copy

gp = graph.Graph(directed=True)
characters = get_data.get_data()

characters_valid = []
house_allegiances = {}

for character in characters:
    if (character['name']):
        # if("Season 6" in character['tvSeries']):
            characters_valid.append(character)
            for house in character['allegiances']:
                if house in house_allegiances:
                    house_allegiances[house].append(character)
                else:
                    house_allegiances[house] = [character]
            gp.add_vertex(character['name'])

for character in characters_valid:
    for house in character['allegiances']:
        for house_char in house_allegiances[house]:
            source_vertex = gp.get_vertex(character['name'])
            destination_vertex = gp.get_vertex(house_char['name'])
            if(source_vertex != destination_vertex):
                gp.add_edge(source_vertex, destination_vertex)

# distance = gp.breadth_first_search(gp.get_vertex('Jon Snow'))

# for character in characters_valid:
#     if len(character['povBooks']) > 0:
#         print(character['name'], ':', distance[gp.get_vertex(character['name'])])

# components = gp.getSCCs()

# for component in components:
#     print(component)
#     print('------------------------')

maior = 0
maior_char = ''
for character in characters_valid:
    new_gp = copy.deepcopy(gp)
    new_gp.remove_vertex(new_gp.get_vertex(character['name']))
    components = new_gp.getSCCs
    if len(components) > maior:
        maior = len(components)
        maior_char = character['name']
print("Maior numero de componentes: ", maior)
print("Personagem ponte: ", maior_char)


# print(len(components))