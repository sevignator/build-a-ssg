from block import markdown_to_html_node


def main() -> None:
    text = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    > Here's a quote for ya.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item

    ```
    Some code goes here
    ```

    1. An ordered list
    2. Is used to display items
    3. In a sequence
    """
    html = markdown_to_html_node(text)
    print(html)


main()
