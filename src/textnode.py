from custom_types import TextType


class TextNode:
    def __init__(
        self,
        text: str,
        text_type: TextType,
        url: str | None = None,
    ) -> None:
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | None = url

        if self.text_type not in ["text", "bold", "italic", "code", "link", "image"]:
            raise ValueError(f'"{self.text_type}" is not a valid text type')

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        contents = f'"{self.text}", "{self.text_type}"'

        if self.url is not None:
            contents += f', "{self.url}"'

        return f"TextNode({contents})"
