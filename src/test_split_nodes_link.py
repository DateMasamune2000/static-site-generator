import unittest

from textnode import TextNode, TextType
from parse import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
	def test_plain(self):
		text = TextNode(text_type=TextType.PLAIN, text="hello, world!")
		nodes = split_nodes_link([text])
		self.assertEqual(nodes, [TextNode("hello, world!", TextType.PLAIN)])

	def test_one_link(self):
		# one link with **no** text following it
		text = TextNode(text_type=TextType.PLAIN, text="hello, [world](https://world.com)")
		nodes = split_nodes_link([text])
		self.assertEqual(nodes, [
			TextNode("hello, ", TextType.PLAIN),
			TextNode("world", TextType.LINK, "https://world.com")
		])

		# one link with text following it
		text = TextNode(text_type=TextType.PLAIN, text="hello, [world](https://world.com)!")
		nodes = split_nodes_link([text])
		self.assertEqual(nodes, [
			TextNode("hello, ", TextType.PLAIN),
			TextNode("world", TextType.LINK, "https://world.com"),
			TextNode("!", TextType.PLAIN)
		])

	def test_multiple_links(self):
		# multiple links with no text preceding first link
		text = TextNode(
			text_type=TextType.PLAIN,
			text="[hello](https://hello.com), [world](https://world.com)!"
		)
		nodes = split_nodes_link([text])
		self.assertEqual(nodes, [
			TextNode("hello", TextType.LINK, "https://hello.com"),
			TextNode(", ", TextType.PLAIN),
			TextNode("world", TextType.LINK, "https://world.com"),
			TextNode("!", TextType.PLAIN)
		])

		# multiple links with no text following last link
		text = TextNode(
			text_type=TextType.PLAIN,
			text="B[hello](https://hello.com), [world](https://world.com)"
		)
		nodes = split_nodes_link([text])
		self.assertEqual(nodes, [
			TextNode("B", TextType.PLAIN),
			TextNode("hello", TextType.LINK, "https://hello.com"),
			TextNode(", ", TextType.PLAIN),
			TextNode("world", TextType.LINK, "https://world.com")
		])

