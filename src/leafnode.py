from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

        if self.value == None:
            raise ValueError("A leaf node must have a value.")

    def to_html(self):
        if self.tag == None:
            return self.value

        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"
