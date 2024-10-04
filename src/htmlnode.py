class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("wait to be overrided")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        attri = []
        for key in self.props:
            attri.append(f' {key}="{self.props[key]}"')
        return "".join(attri)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
        