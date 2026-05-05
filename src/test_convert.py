import unittest

from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode
from convert import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_plain(self):
        plain = TextNode(text_type=TextType.PLAIN, text="hello, world")
        html_node = text_node_to_html_node(plain)
        
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "hello, world")
        self.assertEqual(html_node.to_html(), "hello, world")
        
    def test_bold_italic_code(self):
        bold = TextNode(text_type=TextType.BOLD, text="bold text")
        italic = TextNode(text_type=TextType.ITALIC, text="italic text")
        code = TextNode(text_type=TextType.CODE, text="code snippet")
        
        html_bold = text_node_to_html_node(bold)
        html_italic = text_node_to_html_node(italic)
        html_code = text_node_to_html_node(code)
        
        self.assertEqual(html_bold.tag, "b")
        self.assertEqual(html_italic.tag, "i")
        self.assertEqual(html_code.tag, "code")
        
        self.assertEqual(html_bold.value, "bold text")
        self.assertEqual(html_italic.value, "italic text")
        self.assertEqual(html_code.value, "code snippet")
        
        self.assertEqual(html_bold.to_html(), "<b>bold text</b>")
        self.assertEqual(html_italic.to_html(), "<i>italic text</i>")
        self.assertEqual(html_code.to_html(), "<code>code snippet</code>")
        
    def test_image(self):
        image = TextNode(text_type=TextType.IMAGE, text="justaway", url="https://ginta.ma/justaway.png")
        image_html = text_node_to_html_node(image)
        
        self.assertEqual(image_html.value, "")
        self.assertEqual(image_html.props, {"src":"https://ginta.ma/justaway.png", "alt":"justaway"})
        self.assertEqual(image_html.to_html(), '<img src="https://ginta.ma/justaway.png" alt="justaway"></img>')
        
    def test_link(self):
        link = TextNode(text_type=TextType.LINK, text="gintama", url="https://ginta.ma/index.html")
        link_html = text_node_to_html_node(link)
        
        self.assertEqual(link_html.value, "gintama")
        self.assertEqual(link_html.props, {"href":"https://ginta.ma/index.html"})
        self.assertEqual(link_html.to_html(), '<a href="https://ginta.ma/index.html">gintama</a>')