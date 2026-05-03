class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
        
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join([x+'="'+self.props[x]+'"' for x in self.props])
        
    def __repr__(self):
        return f'"tag":{self.tag},"value":{self.value},"children":{self.children},"props":{self.props}'
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None:
            return self.value
        else:
            if self.props is None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
                
    def __repr__(self):
        return f'"tag":{self.tag},"value":{self.value},"props":{self.props}'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None):
        super().__init__(tag=tag, value=value, children=children, props=props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node cannot have 'None' tag")
        if self.children is None:
            raise ValueError("Parent node has to have children.")
        
        string = []
        
        if self.props is not None:
            string.append(f"<{self.tag} {self.props_to_html()}>")
        else:
            string.append(f"<{self.tag}>")
            
        if self.value is not None:
            string.append(f"{self.value}")
            
        for child in self.children:
            string.append(child.to_html())
            
        string.append(f"</{self.tag}>")
            
        return "".join(string)