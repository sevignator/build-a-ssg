from utils import text_to_textnodes


def main() -> None:
    nodes = text_to_textnodes(
        "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    )
    print(nodes)


main()
