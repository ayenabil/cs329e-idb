import json
from models import db, Heroes, Creators



def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()
    return jsn


def create_char():
    characters = load_json('marvel-heroes.json')

    for c in characters['data']['results']:
        id = c['id']
        name = c['name']
        detail = ''
        wiki = ''
        for urls in c['urls']:
            if urls['type'] == 'detail':
                details = urls['url']
            if urls['type'] == 'wiki':
                wiki = urls['url']

        newCharacter = Heroes(id = id, name = name, details = details, wiki = wiki)
        db.session.add(newCharacter)
        db.session.commit()

    creators = load_json('marvel-creators.json')

    for h in creators['data']['results']:
        id = h['id']
        name = h['fullName']
        for urls in c['urls']:
            if urls['type'] == 'detail':
                details = urls['url']
        newCreator = Creators(id = id, name = name, details = details)
        db.session.add(newCreator)
        db.session.commit()




create_char()