from typing import Literal


Delimiters = Literal["*", "**", "`"]

TextType = Literal["text", "bold", "italic", "code", "link", "image"]

BlockType = Literal[
    "paragraph", "heading", "code", "quote", "unordered_list", "ordered_list"
]
