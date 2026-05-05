from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType

text_node_vals = {
    TextType.PLAIN: None,
    TextType.BOLD: 'b',
    TextType.ITALIC: 'i',
    TextType.CODE: 'code'
}
    
def text_node_to_html_node(text_node):
    if text_node.text_type in text_node_vals:
        tag = text_node_vals[text_node.text_type]
        return LeafNode(tag=tag, value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={'href':text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url,"alt":text_node.text})
        
    return LeafNode(tag=tag, value=value, props=props)