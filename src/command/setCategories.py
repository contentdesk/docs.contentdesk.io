import json
import sys


sys.path.append("..")
from service.markdown import MarkdownService
from service.discover import getCategoryTree
from os import getenv
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


def setCategories(category, parentCategory = None, akeneoCategories = {}, language = 'en_US'):
    # check if category is a list
    if isinstance(category, list):
        for cat in category:
            print("Category: ")
            print(cat['identifier'])
            print(cat['name'])
            if cat['identifier'] not in akeneoCategories:
                akeneoCategories[cat['identifier']] = {}
            akeneoCategories[cat['identifier']]["code"] = cat['identifier']
            akeneoCategories[cat['identifier']]["parent"] = parentCategory
            if 'labels' not in akeneoCategories[cat['identifier']]:
                akeneoCategories[cat['identifier']]["labels"] = {}
            akeneoCategories[cat['identifier']]["labels"][language] = cat['name']
            if 'children' in cat:
                setCategories(cat['children'], cat['identifier'], akeneoCategories, language)
    else:
        print("Category: ")
        print(category['identifier'])
        print(category['name'])
        if category['identifier'] not in akeneoCategories:
            akeneoCategories[category['identifier']] = {}
        akeneoCategories[category['identifier']]["code"] = category['identifier']
        akeneoCategories[category['identifier']]["parent"] = parentCategory
        if 'labels' not in akeneoCategories[category['identifier']]:
            akeneoCategories[category['identifier']]["labels"] = {}
        akeneoCategories[category['identifier']]["labels"][language] = category['name']
        if 'children' in category:
            setCategories(category['children'], category['identifier'], akeneoCategories, language)

    return akeneoCategories

def main():
    category = 'sui_root'
    categoriesEN = getCategoryTree(category, 'en')
    categoriesDE = getCategoryTree(category, 'de')
    categoriesFR = getCategoryTree(category, 'fr')
    categoriesIT = getCategoryTree(category, 'it')
    
    # DEBUG
    with open("../../output/discover/categories/categoriesEN.json", "w") as file:
        json.dump(categoriesEN, file, indent=4)
    with open("../../output/discover/categories/categoriesDE.json", "w") as file:
        json.dump(categoriesDE, file, indent=4)
    with open("../../output/discover/categories/categoriesFR.json", "w") as file:
        json.dump(categoriesFR, file, indent=4)
    with open("../../output/discover/categories/categoriesIT.json", "w") as file:
        json.dump(categoriesIT, file, indent=4)

    akeneoCategories = setCategories(categoriesEN)
    akeneoCategories = setCategories(categoriesDE, None, akeneoCategories, 'de_CH')
    akeneoCategories = setCategories(categoriesFR, None, akeneoCategories, 'fr_FR')
    akeneoCategories = setCategories(categoriesIT, None, akeneoCategories, 'it_IT')
    
    # DEBUG
    with open("../../output/akeneo/categories/categories.json", "w") as file:
        json.dump(akeneoCategories, file, indent=4)
        
    # Compare
    with open("../../docs/schema/categories.csv", "w", encoding='utf-8') as file:
        for code, body in akeneoCategories.items():
            parent = body['parent'] if body['parent'] else ''
            en = body['labels']['en_US'] if 'en_US' in body['labels'] else ''
            de = body['labels']['de_CH'] if 'de_CH' in body['labels'] else ''
            fr = body['labels']['fr_FR'] if 'fr_FR' in body['labels'] else ''
            it = body['labels']['it_IT'] if 'it_IT' in body['labels'] else ''
            file.write(f"{code};{parent};{en};{de};{fr};{it}\n")
        
    # Create markdown file
    MarkdownService.createCategoriesIndexMarkdown(akeneoCategories)

if __name__ == "__main__":
    main()
