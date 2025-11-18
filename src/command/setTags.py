import json
import sys
sys.path.append("..")

from service.discover import getAllTags
from service.markdown import MarkdownService
from os import getenv
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

def setTags(tags, simpleTags = {}, language = 'en_US', parent = None):
    # check if category is a list
    if isinstance(tags, list):
        for tag in tags:
            print("Tag: ")
            print(tag['identifier'])
            print(tag['name'])
            if tag['additionalType'] not in simpleTags:
                simpleTags[tag['additionalType']] = {}
            simpleTags[tag['additionalType']]["code"] = tag['identifier']
            simpleTags[tag['additionalType']]["parent"] = tag['additionalType']
            if 'labels' not in simpleTags[tag['additionalType']]:
                simpleTags[tag['additionalType']]["labels"] = {}
            simpleTags[tag['additionalType']]["labels"][language] = tag['name']
            if 'lastModified' in tag:
                simpleTags[tag['additionalType']]["lastModified"] = tag['lastModified']
    else:
        print("tag: ")
        print(tags['identifier'])
        print(tags['name'])

    return simpleTags

def main():
    tagsEN = getAllTags('en')
    tagsDE = getAllTags('de')
    tagsFR = getAllTags('fr')
    tagsIT = getAllTags('it')
    
    # DEBUG
    with open("../../output/discover/tags/tagsEN.json", "w") as file:
        json.dump(tagsEN, file, indent=4)
    with open("../../output/discover/tags/tagsDE.json", "w") as file:
        json.dump(tagsDE, file, indent=4)
    with open("../../output/discover/tags/tagsFR.json", "w") as file:
        json.dump(tagsFR, file, indent=4)
    with open("../../output/discover/tags/tagsIT.json", "w") as file:
        json.dump(tagsIT, file, indent=4)

    simpleTags = setTags(tagsEN)
    simpleTags = setTags(tagsDE, simpleTags, 'de_CH')
    simpleTags = setTags(tagsFR, simpleTags, 'fr_FR')
    simpleTags = setTags(tagsIT, simpleTags, 'it_IT')

    # replace "-" with "" in key fields
    simpleTags = {k.replace("-", ""): v for k, v in simpleTags.items()}
            
    # Compare
    with open("../../docs/schema/types.csv", "w", encoding='utf-8') as file:
        for code, body in simpleTags.items():
            parent = body['parent'] if body['parent'] else ''
            en = body['labels']['en_US'] if 'en_US' in body['labels'] else ''
            de = body['labels']['de_CH'] if 'de_CH' in body['labels'] else ''
            fr = body['labels']['fr_FR'] if 'fr_FR' in body['labels'] else ''
            it = body['labels']['it_IT'] if 'it_IT' in body['labels'] else ''
            lastModified = body['lastModified'] if 'lastModified' in body else ''
            file.write(f"{code};{parent};{en};{de};{fr};{it};{lastModified}\n")
            
    # Create markdown file
    MarkdownService.createTagIndexMarkdown(simpleTags)

if __name__ == "__main__":
    main()
