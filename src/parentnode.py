from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(
        self,
        tag: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag=tag, props=props)

        if self.children is None:
            self.children: list[HTMLNode] = children

        if self.tag is None:
            raise ValueError("A parent node must have a tag.")

        if self.children is None:
            raise ValueError("A parent node must have children.")

    def to_html(self):
        children_html = "".join(map(lambda node: node.to_html(), self.children))

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
