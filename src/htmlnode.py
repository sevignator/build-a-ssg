class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        kv_pairs = []

        for _, key in enumerate(self.props):
            value = self.props[key]
            kv_pairs.append(f' {key}="{value}"')

        return "".join(kv_pairs)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
