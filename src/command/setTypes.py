import json
import sys
sys.path.append("..")

from service.discover import getTypesTree
from service.markdown import MarkdownService
from os import getenv
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

def setTypes(types, akeneoTypes = {}, language = 'en_US', parent = None):
    # check if category is a list
    if isinstance(types, list):
        for typ in types:
            print("Type: ")
            print(typ['entityType'])
            print(typ['name'])
            if 'additionalType' in typ:
                if typ['additionalType'] not in akeneoTypes:
                    akeneoTypes[typ['additionalType']] = {}
                akeneoTypes[typ['additionalType']]["code"] = typ['additionalType']
                akeneoTypes[typ['additionalType']]["parent"] = parent
                if 'labels' not in akeneoTypes[typ['additionalType']]:
                    akeneoTypes[typ['additionalType']]["labels"] = {}
                akeneoTypes[typ['additionalType']]["labels"][language] = typ['name']
                if 'types' in typ:
                    setTypes(typ['types'], akeneoTypes, language, typ['entityType'])
            else:
                if typ['entityType'] not in akeneoTypes:
                    akeneoTypes[typ['entityType']] = {}
                akeneoTypes[typ['entityType']]["code"] = typ['entityType']
                akeneoTypes[typ['entityType']]["parent"] = parent
                if 'labels' not in akeneoTypes[typ['entityType']]:
                    akeneoTypes[typ['entityType']]["labels"] = {}
                akeneoTypes[typ['entityType']]["labels"][language] = typ['name']
                if 'types' in typ:
                    setTypes(typ['types'], akeneoTypes, language, typ['entityType'])
    else:
        print("Type: ")
        print(types['entityType'])
        print(types['name'])
        if types['entityType'] not in akeneoTypes:
            akeneoTypes[types['entityType']] = {}
        akeneoTypes[types['entityType']]["code"] = types['entityType']
        akeneoTypes[types['entityType']]["parent"] = parent
        if 'labels' not in akeneoTypes[types['entityType']]:
            akeneoTypes[types['entityType']]["labels"] = {}
        akeneoTypes[types['entityType']]["labels"][language] = types['name']
        if 'types' in types:
            setTypes(types['types'], akeneoTypes, language)

    return akeneoTypes

def main():
    typesEN = getTypesTree('en')
    typesDE = getTypesTree('de')
    typesFR = getTypesTree('fr')
    typesIT = getTypesTree('it')
    
    # DEBUG
    with open("../../output/discover/types/typesEN.json", "w") as file:
        json.dump(typesEN, file, indent=4)
    with open("../../output/discover/types/typesDE.json", "w") as file:
        json.dump(typesDE, file, indent=4)
    with open("../../output/discover/types/typesFR.json", "w") as file:
        json.dump(typesFR, file, indent=4)
    with open("../../output/discover/types/typesIT.json", "w") as file:
        json.dump(typesIT, file, indent=4)

    akeneoTypes = setTypes(typesEN)
    akeneoTypes = setTypes(typesDE, akeneoTypes, 'de_CH')
    akeneoTypes = setTypes(typesFR, akeneoTypes, 'fr_FR')
    akeneoTypes = setTypes(typesIT, akeneoTypes, 'it_IT')

    # replace "-" with "" in key fields
    akeneoTypes = {k.replace("-", ""): v for k, v in akeneoTypes.items()}

    # DEBUG
    with open("../../output/akeneo/family/families.json", "w") as file:
        json.dump(akeneoTypes, file, indent=4)

    # Save as csv with UTF-8 encoding and replace "None" in every field with empty string
    with open("../../output/akeneo/family/families.csv", "w", encoding='utf-8') as file:
        for code, body in akeneoTypes.items():
            parent = body['parent'] if body['parent'] else ''
            en = body['labels']['en_US'] if 'en_US' in body['labels'] else ''
            de = body['labels']['de_CH'] if 'de_CH' in body['labels'] else ''
            fr = body['labels']['fr_FR'] if 'fr_FR' in body['labels'] else ''
            it = body['labels']['it_IT'] if 'it_IT' in body['labels'] else ''
            file.write(f"{code};{parent};{en};{de};{fr};{it}\n")
            
    # Compare
    with open("../../docs/schema/types.csv", "w", encoding='utf-8') as file:
        for code, body in akeneoTypes.items():
            parent = body['parent'] if body['parent'] else ''
            en = body['labels']['en_US'] if 'en_US' in body['labels'] else ''
            de = body['labels']['de_CH'] if 'de_CH' in body['labels'] else ''
            fr = body['labels']['fr_FR'] if 'fr_FR' in body['labels'] else ''
            it = body['labels']['it_IT'] if 'it_IT' in body['labels'] else ''
            file.write(f"{code};{parent};{en};{de};{fr};{it}\n")
            
    # Create markdown file
    MarkdownService.createTypeIndexMarkdown(akeneoTypes)

if __name__ == "__main__":
    main()
