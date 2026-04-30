import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_single(self):
        node = HTMLNode(tag="tag", value="value", props={"key":"value"})
        self.assertEqual(node.props_to_html(), "key=value")
        
    def test_props_multiple(self):
        node = HTMLNode(tag="tag", value="value", props={"key1":"value1","key2":"value2"})
        self.assertEqual(node.props_to_html(), "key1=value1 key2=value2")
        
    def test_props_none(self):
        node = HTMLNode(tag="tag", value="value")
        self.assertEqual(node.props_to_html(), "")
        
if __name__ == "__main__":
    unittest.main()