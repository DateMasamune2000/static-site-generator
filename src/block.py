from enum import Enum 
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

g_heading_block = re.compile("^##?#?#?#?#? ")

def block_to_block_type(block):
    block_lines = block.split("\n")

    if len(block_lines) == 1 and g_heading_block.match(block):
        return BlockType.HEADING

    if block[0:4] == "```\n" and block[-5:] == "\n```\n":
        return BlockType.CODE

    is_quote = True
    for line in block_lines:
        if line[0] != ">":
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    is_unordered_list = True
    for line in block_lines:
        if line[0:2] != "- ":
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.UNORDERED_LIST

    current_index = 1
    is_ordered_list = True
    for line in block_lines:
        if line[0] not in "0123456789" or int(line[0]) != current_index or line[1] != '.':
            is_ordered_list = False
            break
        current_index += 1
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
