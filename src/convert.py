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
    BlockType.UNORDERED_LIST: 'ul',
}

def strip_bullet(line):
    if line.startswith("- ") or line.startswith("> "):
        return line[2:]
    elif line[0].isdigit() and line[1] == "." and line[2] == " ":
        return line[3:]
    else:
        return line

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root = ParentNode(tag="div", children=[])

    for block in blocks:
        btype = block_to_block_type(block)
        node = None
        if btype == BlockType.ORDERED_LIST or btype == BlockType.UNORDERED_LIST:
            lines = map(strip_bullet, block.split("\n"))
            children_list = list(map(text_to_children, lines))
            node = ParentNode(
                tag=blocktype_to_tag[block_to_block_type(block)],
                children= map(
                    lambda ø: ParentNode(tag="li", children=ø),
                    children_list)
            )
        elif btype == BlockType.CODE:
            node = ParentNode(
                tag="pre",
                children=[LeafNode(tag="code", value=block[4:-3])]
            )
        elif btype == BlockType.QUOTE:
            node = LeafNode(
                tag="blockquote",
                value=strip_bullet(block)
            )
        elif btype == BlockType.HEADING:
            hsize, txt = block.split(" ", maxsplit=1)
            heading_size = len(hsize)
            node = LeafNode(
                tag=f"h{heading_size}",
                value=txt
            )
        else:
            node = ParentNode(
                tag=blocktype_to_tag[block_to_block_type(block)],
                children=text_to_children(block)
            )
        root.children.append(node)

    return root

def text_to_children(text):
    return [ text_node_to_html_node(n) for n in text_to_textnodes(text) ]

def text_node_to_html_node(text_node):
    if text_node.text_type in text_node_vals:
        tag = text_node_vals[text_node.text_type]
        return LeafNode(tag=tag, value=text_node.text.replace("\n", " "))
        return LeafNode(tag=f"h{heading_size}", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={'href':text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url,"alt":text_node.text})
        
    return LeafNode(tag="unknown_tag", value="", props={})

