import unittest

from block import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):
    def test_heading(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = " # heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        block = """# heading
some text
"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        block = "## heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "###### heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "####### heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        block = """```
this is some code
```
"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = """```
this is some code
"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        block = """This is some text
```
this is some code
```
"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        block = "```This is some code```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote(self):
        block = """>be me
>neighbors are beekeepers
>see a cheap diesel mercedes listed for $3000
>think it's a steal
>try to bargain down to $2900
>seller agrees
>i drive home in the car
>neighbors suddenly lose their business to wasps
>i pay it no heed, the area I'm living in has a wasp problem anyway
>car doesn't start one day
>i open the hood
>wasps sting me in the face
>i go to the hospital
>wasps have built a nest in my house
>i need to pay $500 to get the damn things out of the house"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        block = """>be me
>neighbors are beekeepers
>see a cheap diesel mercedes listed for $3000
>think it's a steal
>try to bargain down to $2900
>seller agrees
>i drive home in the car
>neighbors suddenly lose their business to wasps
>i pay it no heed, the area I'm living in has a wasp problem anyway
>car doesn't start one day
>i open the hood
>wasps sting me in the face
>i go to the hospital
>wasps have built a nest in my house
>i need to pay $500 to get the damn things out of the house
am never buying a used car again"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = """- this
- is
- a
- list"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        block = """- this
- is
- a
- list
NOT"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = """1. this
2. is
3. a
4. list"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

        block = """1. this
2. is
3. not
4. a
2. list"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        block = """1. this
2. is
3. not
4. a
5. list
either"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = """This is a paragraph.
This paragraph has some text."""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
