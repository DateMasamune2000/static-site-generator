import unittest

from htmlnode import LeafNode

class test_leafnode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "hello, world")
        self.assertEqual(node.to_html(), "<p>hello, world</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "hello, world", {"href":"http://boot.dev"})
        self.assertEqual(node.to_html(), "<a href=\"http://boot.dev\">hello, world</a>")
    
    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "hello, world", None)
        self.assertEqual(node.to_html(), "hello, world")