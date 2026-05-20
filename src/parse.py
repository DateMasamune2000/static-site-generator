import re
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType

text_node_delims = {
    TextType.BOLD: '**',
    TextType.ITALIC: '_',
    TextType.CODE: '`',
}

def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.strip().split("\n\n"):
        s = block.strip()
        if len(s) != 0:
            blocks.append(s)
    return blocks

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAIN)]
    for t in text_node_delims:
        nodes = split_nodes_delimiter(nodes, text_node_delims[t], t)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        l = old_node.text.split(delimiter)

        if len(l) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax at '{old_node.text}'")

        for i, x in enumerate(l):
            if i % 2 == 0:
                new_nodes.append(TextNode(x, TextType.PLAIN))
            else:
                new_nodes.append(TextNode(x, text_type))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\]]*)\]\(([^\)]+)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\]]*)\]\(([^\)]+)\)", text)

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)
        ctext = old_node.text

        for txt, href in links:
            link_text = f"[{txt}]({href})"
            temp = ctext.split(link_text)
            if len(temp[0]) > 0:
                new_nodes.append(TextNode(temp[0], old_node.text_type))
            new_nodes.append(TextNode(txt, TextType.LINK, href))
            ctext = temp[1]

        if len(ctext) > 0:
            new_nodes.append(TextNode(ctext, old_node.text_type))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        ctext = old_node.text

        for txt, src in images:
            image_text = f"![{txt}]({src})"
            temp = ctext.split(image_text)
            if len(temp[0]) > 0:
                new_nodes.append(TextNode(temp[0], old_node.text_type))
            new_nodes.append(TextNode(text=txt, text_type=TextType.IMAGE, url=src))
            ctext = temp[1]

        if len(ctext) > 0:
            new_nodes.append(TextNode(ctext, old_node.text_type))

    return new_nodes
