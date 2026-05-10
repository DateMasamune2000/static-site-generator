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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []

	for old_node in old_nodes:
		if old_node.text_type != TextType.PLAIN:
			new_nodes.append(old_node)

		l = old_node.text.split(delimiter)

		if len(l) % 2 == 0:
			raise("Invalid Markdown syntax")

		for i, x in enumerate(l):
			if i % 2 == 0:
				new_nodes.append(TextNode(x, TextType.PLAIN))
			else:
				new_nodes.append(TextNode(x, text_type))

	return new_nodes
