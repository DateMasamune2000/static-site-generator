from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from parse import markdown_to_blocks, text_to_textnodes
from block import block_to_block_type, BlockType

text_node_vals = {
    TextType.PLAIN: None,
    TextType.BOLD: 'b',
    TextType.ITALIC: 'i',
    TextType.CODE: 'code'
}

blocktype_to_tag = {
    BlockType.PARAGRAPH: 'p',
    BlockType.CODE: 'code',
    BlockType.ORDERED_LIST: 'ol',
    BlockType.UNORDERED_LIST: 'ul'
}

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root = ParentNode(tag="div", children=[])

    for block in blocks:
        btype = block_to_block_type(block)
        node = None
        if btype != BlockType.CODE:
            node = ParentNode(
                tag=blocktype_to_tag[block_to_block_type(block)],
                children=text_to_children(block)
            )
        else:
            node = ParentNode(
                tag="pre",
                children=[LeafNode(tag="code", value=block[4:-3])]
            )
        root.children.append(node)

    return root

def text_to_children(text):
    return [ text_node_to_html_node(n) for n in text_to_textnodes(text) ]

def text_node_to_html_node(text_node):
    if text_node.text_type in text_node_vals:
        tag = text_node_vals[text_node.text_type]
        return LeafNode(tag=tag, value=text_node.text.replace("\n", " "))
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={'href':text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url,"alt":text_node.text})
        
    return LeafNode(tag="unknown_tag", value="", props={})

