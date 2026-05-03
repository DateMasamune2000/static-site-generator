import unittest

from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_parent_grandchild(self):
        grandchild_node = LeafNode("span", "grandchild", props={"class":"abcd"})
        child_node = ParentNode("p", [grandchild_node], value="child")
        parent_node = ParentNode("div", [child_node], value="parent")
        self.assertEqual(parent_node.to_html(), "<div>parent<p>child<span class=\"abcd\">grandchild</span></p></div>")
        
    def test_parent_children(self):
        child1 = LeafNode("span", "child1")
        child2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span></div>")
        
    def test_parent_grandchildren(self):
        grandchild_node = LeafNode("span", "grandchild", props={"class":"abcd"})
        child_node = LeafNode("b", "child1")
        child2_node = ParentNode("p", [grandchild_node], value="child2")
        parent_node = ParentNode("div", [child_node,child2_node], value="parent")
        self.assertEqual(parent_node.to_html(), "<div>parent<b>child1</b><p>child2<span class=\"abcd\">grandchild</span></p></div>")