import os

class MarkdownService:
    
    def createTypeIndexMarkdown(typesData):
        print("Creating type index markdown...")
        """
        Create markdown content for a given type data.
        """
        output_dir = os.path.join(os.path.dirname(__file__), '../../docs/schema/')
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, f'types.md'), "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write("hide:\n")
            f.write("  - navigation\n")
            f.write("  - toc\n")
            f.write("---\n")
            f.write(f"# Types\n\n")
            f.write("<div class=\"grid cards\" markdown>\n\n")
            f.write("- :fontawesome-solid-file-csv: [CSV Export](https://docs.contentdesk.io/schema/types.csv)\n")
            f.write("- :octicons-git-compare-16: [Compare CSV](https://github.com/contentdesk/docs.contentdesk.io/blob/main/docs/schema/types.csv)\n")
            f.write("</div>\n\n")
            f.write("""<table id="charts-table" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Code</th>
                <th>Name DE</th>
                <th>Parent</th>
                <th>Name EN</th>
                <th>Name FR</th>
                <th>Name IT</th>
                
            </tr>
        </thead>
        <tbody>
    """)
            for typeItem in typesData:
                #print(typesData)
                print (typeItem)
                f.write(f"<tr>\n")
                f.write(f"<td>{typesData[typeItem]['code']}</td>\n")
                f.write(f"<td>{typesData[typeItem]['labels'].get('de_CH', '')}</td>\n")
                if typesData[typeItem]['parent'] is None or typesData[typeItem]['parent'] == "None":
                    f.write(f"<td></td>\n")
                else:
                    f.write(f"<td>{typesData[typeItem]['parent']}</td>\n")
                f.write(f"<td>{typesData[typeItem]['labels'].get('en_US', '')}</td>\n")
                f.write(f"<td>{typesData[typeItem]['labels'].get('fr_FR', '')}</td>\n")
                f.write(f"<td>{typesData[typeItem]['labels'].get('it_IT', '')}</td>\n")
                f.write(f"</tr>\n")
            f.write(f"</tbody>\n</table>\n")
        print("Markdown file 'types.md' created.")
        
    def createCategoriesIndexMarkdown(categoriesData):
        print("Creating categories index markdown...")
        """
        Create markdown content for a given categories data.
        """
        output_dir = os.path.join(os.path.dirname(__file__), '../../docs/schema/')
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, f'categories.md'), "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write("hide:\n")
            f.write("  - navigation\n")
            f.write("  - toc\n")
            f.write("---\n")
            f.write(f"# Categories\n\n")
            f.write("<div class=\"grid cards\" markdown>\n\n")
            f.write("- :fontawesome-solid-file-csv: [CSV Export](https://docs.contentdesk.io/schema/categories.csv)\n")
            f.write("- :octicons-git-compare-16: [Compare CSV](https://github.com/contentdesk/docs.contentdesk.io/blob/main/docs/schema/categories.csv)\n")
            f.write("</div>\n\n")
            f.write("""<table id="charts-table" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Code</th>
                <th>Name DE</th>
                <th>Parent</th>
                <th>Name EN</th>
                <th>Name FR</th>
                <th>Name IT</th>
                
            </tr>
        </thead>
        <tbody>
    """)
            for categoryItem in categoriesData:
                #print(categoriesData)
                print (categoryItem)
                f.write(f"<tr>\n")
                f.write(f"<td>{categoriesData[categoryItem]['code']}</td>\n")
                f.write(f"<td>{categoriesData[categoryItem]['labels'].get('de_CH', '')}</td>\n")
                if categoriesData[categoryItem]['parent'] is None or categoriesData[categoryItem]['parent'] == "None":
                    f.write(f"<td></td>\n")
                else:
                    f.write(f"<td>{categoriesData[categoryItem]['parent']}</td>\n")
                f.write(f"<td>{categoriesData[categoryItem]['labels'].get('en_US', '')}</td>\n")
                f.write(f"<td>{categoriesData[categoryItem]['labels'].get('fr_FR', '')}</td>\n")
                f.write(f"<td>{categoriesData[categoryItem]['labels'].get('it_IT', '')}</td>\n")
                f.write(f"</tr>\n")
            f.write(f"</tbody>\n</table>\n")
        print("Markdown file 'categories.md' created.")
    
    def createAmenityFeaturesIndexMarkdown(amenityFeaturesData):
        print("Creating amenity features index markdown...")
        """
        Create markdown content for a given amenity features data.
        """
        output_dir = os.path.join(os.path.dirname(__file__), '../../docs/schema/')
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, f'amenityFeatures.md'), "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write("hide:\n")
            f.write("  - navigation\n")
            f.write("  - toc\n")
            f.write("---\n")
            f.write(f"# Amenity Features\n\n")
            f.write("<div class=\"grid cards\" markdown>\n\n")
            f.write("- :fontawesome-solid-file-csv: [CSV Export](https://docs.contentdesk.io/schema/amenityFeatures.csv)\n")
            f.write("- :octicons-git-compare-16: [Compare CSV](https://github.com/contentdesk/docs.contentdesk.io/blob/main/docs/schema/amenityFeatures.csv)\n")
            f.write("</div>\n\n")
            f.write("""<table id="charts-table" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Code</th>
                <th>Name DE</th>
                <th>Parent</th>
                <th>Name EN</th>
                <th>Name FR</th>
                <th>Name IT</th>
                <th>Value Type</th>
            </tr>
        </thead>
        <tbody>
    """)
            for featureItem in amenityFeaturesData:
                #print(amenityFeaturesData)
                print (featureItem)
                f.write(f"<tr>\n")
                f.write(f"<td>{amenityFeaturesData[featureItem]['code']}</td>\n")
                f.write(f"<td>{amenityFeaturesData[featureItem]['labels'].get('de_DE', '')}</td>\n")
                if 'parent' not in amenityFeaturesData[featureItem]:
                    f.write(f"<td></td>\n")
                else:
                    f.write(f"<td>{amenityFeaturesData[featureItem]['parent']}</td>\n")
                f.write(f"<td>{amenityFeaturesData[featureItem]['labels'].get('en_US', '')}</td>\n")
                f.write(f"<td>{amenityFeaturesData[featureItem]['labels'].get('fr_FR', '')}</td>\n")
                f.write(f"<td>{amenityFeaturesData[featureItem]['labels'].get('it_IT', '')}</td>\n")
                if 'valueType' not in amenityFeaturesData[featureItem]:
                    f.write(f"<td></td>\n")
                else:
                    f.write(f"<td>{amenityFeaturesData[featureItem]['valueType']}</td>\n")
                f.write(f"</tr>\n")
            f.write(f"</tbody>\n</table>\n")
        print("Markdown file 'amenityFeatures.md' created.")