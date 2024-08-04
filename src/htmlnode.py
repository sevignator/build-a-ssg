class HTMLNode:

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list | None = children
        self.props: dict[str, str] | None = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        kv_pairs = []

        for _, key in enumerate(self.props):
            value = self.props[key]
            kv_pairs.append(f' {key}="{value}"')

        return "".join(kv_pairs)

    def __repr__(self):
        return f'HTMLNode("{self.tag}", "{self.value}", {self.children}, {self.props})'
