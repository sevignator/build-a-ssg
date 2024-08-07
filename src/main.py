# import os

from functions.extract_title import extract_title

# from functions.copy_source_to_dest import copy_source_to_dest


def main() -> None:
    # current_dir = os.path.dirname(__file__)
    # root_dir = os.path.dirname(current_dir)
    # source_dir = os.path.join(root_dir, "static")
    # dest_dir = os.path.join(root_dir, "public")

    # copy_source_to_dest(source_dir, dest_dir)

    title = extract_title(
        """    # This is amazing

- Item 1
- Item 2
- Item 3

Something else"""
    )
    print(title)


if __name__ == "__main__":
    main()
