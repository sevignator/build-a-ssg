from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

        if self.tag == None:
            raise ValueError("A parent node must have a tag.")

        if self.children == None:
            raise ValueError("A parent node must have children.")

    def to_html(self):
        children_html = "".join(map(lambda node: node.to_html(), self.children))

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
