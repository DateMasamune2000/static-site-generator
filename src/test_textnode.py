import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_neq_text(self):
        node = TextNode("a", TextType.PLAIN)
        node2 = TextNode("b", TextType.PLAIN)
        self.assertNotEqual(node, node2)
        
    def test_neq_type(self):
        node = TextNode("a", TextType.PLAIN)
        node2 = TextNode("a", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_neq_url(self):
        node = TextNode("a", TextType.LINK, "abcd")
        node2 = TextNode("a", TextType.LINK, "cdef")
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()