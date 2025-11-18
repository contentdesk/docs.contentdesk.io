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
                print (typeItem)
                f.write(f"<tr>\n")
                f.write(f"<td>{typeItem.get('code', '')}</td>\n")
                f.write(f"<td>{typeItem.get('name_de', '')}</td>\n")
                f.write(f"<td>{typeItem.get('parent', '')}</td>\n")
                f.write(f"<td>{typeItem.get('name_en', '')}</td>\n")
                f.write(f"<td>{typeItem.get('name_fr', '')}</td>\n")
                f.write(f"<td>{typeItem.get('name_it', '')}</td>\n")
                f.write(f"</tr>\n")
            f.write(f"</tbody>\n</table>\n")
        print("Markdown file 'types.md' created.")