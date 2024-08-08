import re

from functions.extract_title import extract_title
from functions.markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    """Converts a Markdown file into an HTML file"""

    dest_path_html = re.sub(r"\.\w+$", ".html", dest_path)

    print(f"Generating page from {from_path} to {dest_path_html} using {template_path}")

    # Handle Markdown (source) file logic
    with open(from_path, "r", encoding="utf-8") as from_file:
        from_contents = from_file.read()
        from_html = markdown_to_html_node(from_contents).to_html()
        from_title = extract_title(from_contents)
        from_file.close()

    # Handle template file logic
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_contents = template_file.read()
        template_with_title = template_contents.replace("{{ Title }}", from_title)
        template_with_content = template_with_title.replace("{{ Content }}", from_html)
        template_file.close()

    # Handle HTML (destination) file logic
    with open(dest_path_html, "w", encoding="utf-8") as dest_file:
        dest_file.write(template_with_content)
        dest_file.close()
