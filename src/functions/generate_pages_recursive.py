import os

from functions.generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """Recursively generates HTML pages from Markdown documents"""

    dir_content = os.listdir(dir_path_content)

    # Iterate over each entry in the current directory
    for entry in dir_content:
        src_entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)

        # Create HTML file
        if os.path.isfile(src_entry_path):
            generate_page(src_entry_path, template_path, dest_entry_path)
            continue

        # Create destination directory if it doesn't already exist
        if not os.path.isdir(dest_entry_path):
            os.mkdir(dest_entry_path)

        # Recursively handle directory traversal
        generate_pages_recursive(src_entry_path, template_path, dest_entry_path)
