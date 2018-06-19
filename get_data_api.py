import anapioficeandfire
import json
import re

api = anapioficeandfire.API()

books = api.get_books()

data = []

# Get all books
for book in books:

    # Get data of all characters in the book
    for character in book.characters:
        # get the character ID
        characterId = re.search(r'(\d+)$', character).group(1)
        if characterId:
            characterData = api.get_character(id=characterId)
            allegiances = []

            # Get all houses that character follow
            for allegiance in characterData.allegiances:
                # get the house ID
                # print(allegiance)
                allegianceId = re.search('(\d+)$', allegiance).group(1)
                if allegianceId:
                    # print(allegianceId)
                    house = api.get_house(id=allegianceId)
                    allegiances.append(house.name)

            # Save data
            newCharacter = {
                "url": characterData.url,
                "name": characterData.name,
                "gender": characterData.gender,
                "culture": characterData.culture,
                "born": characterData.born,
                "died": characterData.died,
                "titles": characterData.titles,
                "aliases": characterData.aliases,
                "father": characterData.father,
                "mother": characterData.mother,
                "spouse": characterData.spouse,
                "allegiances": allegiances,
                "books": characterData.books,
                "povBooks": characterData.povBooks,
                "tvSeries": characterData.tvSeries,
                "playedBy": characterData.playedBy
            }

            # don't put equals characters in the data
            if newCharacter not in data:
                data.append(newCharacter)

with open('data.json', 'w') as outfile:  
    json.dump(data, outfile)