import os

from functions.copy_source_to_dest import copy_source_to_dest
from functions.generate_page import generate_page

# from functions.copy_source_to_dest import copy_source_to_dest


def main() -> None:
    current_dir_path = os.path.dirname(__file__)
    root_dir_path = os.path.dirname(current_dir_path)
    static_dir_path = os.path.join(root_dir_path, "static")
    public_dir_path = os.path.join(root_dir_path, "public")
    content_dir_path = os.path.join(root_dir_path, "content")

    copy_source_to_dest(static_dir_path, public_dir_path)

    generate_page(
        os.path.join(content_dir_path, "index.md"),
        os.path.join(root_dir_path, "template.html"),
        os.path.join(public_dir_path, "index.html"),
    )


if __name__ == "__main__":
    main()
