from htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag=tag, value=value, props=props)

        if self.value is None:
            raise ValueError("A leaf node must have a value.")

    def to_html(self):
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
